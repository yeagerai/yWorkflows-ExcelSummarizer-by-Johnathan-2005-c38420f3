
import os
import pytest
from tempfile import NamedTemporaryFile
from openpyxl import Workbook
from pandas.testing import assert_frame_equal

from your_project_path.components.excel_workbook_reader import (
    ExcelWorkbookReader,
    ExcelWorkbookReaderInputDict,
    ExcelWorkbookReaderOutputDict,
)

# Mocked input data and expected output data
test_cases = [
    {
        "excel_file_path": None,  # Will be replaced with a temporary file path later
        "use_pandas": True,
        "expected_output": {"Sheet1": {"A1": "Hello", "B1": "World"}},
    },
    {
        "excel_file_path": None,  # Will be replaced with a temporary file path later
        "use_pandas": False,
        "expected_output": {"Sheet1": {"A1": "Hello", "B1": "World"}},
    },
]

@pytest.fixture(scope="function")
def create_temp_excel_file():
    with NamedTemporaryFile(delete=False, suffix=".xlsx") as temp_file:
        wb = Workbook()
        sheet = wb.active
        sheet["A1"] = "Hello"
        sheet["B1"] = "World"
        wb.save(temp_file.name)
        yield temp_file.name
        os.unlink(temp_file.name)

@pytest.mark.parametrize("test_case", test_cases)
def test_transform(create_temp_excel_file, test_case):
    # Set the temporary file path in the test case
    test_case["excel_file_path"] = create_temp_excel_file

    # Prepare the input data
    input_data = ExcelWorkbookReaderInputDict(excel_file_path=test_case["excel_file_path"])

    # Modify the component configuration to use the desired library
    component = ExcelWorkbookReader()
    component.library_choice = "pandas" if test_case["use_pandas"] else "openpyxl"

    # Call the component's transform() method
    output_data = component.transform(input_data)

    # Assert that the output matches the expected output
    if test_case["use_pandas"]:
        for sheet_name, expected_df_dict in test_case["expected_output"].items():
            assert_frame_equal(
                output_data.workbook_data[sheet_name],
                expected_df_dict,
                check_names=True,
                check_index_type=True,
                check_dtype=True,
            )
    else:
        for sheet_name, expected_cells_dict in test_case["expected_output"].items():
            for cell_key, expected_value in expected_cells_dict.items():
                assert (
                    output_data.workbook_data[sheet_name][cell_key].value == expected_value
                )

@pytest.mark.parametrize(
    "invalid_library_choice",
    ["invalid_choice", "unsupported", "something else"],
)
def test_invalid_library_choice(create_temp_excel_file, invalid_library_choice):
    input_data = ExcelWorkbookReaderInputDict(excel_file_path=create_temp_excel_file)
    component = ExcelWorkbookReader()
    component.library_choice = invalid_library_choice

    with pytest.raises(ValueError):
        component.transform(input_data)
