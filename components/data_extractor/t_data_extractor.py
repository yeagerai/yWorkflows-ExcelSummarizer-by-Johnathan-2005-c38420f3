
import pytest
import yaml
from pydantic import BaseModel
from components.data_extractor import (
    DataExtractor,
    DataExtractorInputDict,
    DataExtractorOutputDict,
)

# Define test cases with mocked input and expected output data
test_cases = [
    (
        DataExtractorInputDict(input_workbook={"column1": [1, 2], "column2": [3, 4]}),
        DataExtractorOutputDict(processed_data={"key": "value"}),
    ),
    (
        DataExtractorInputDict(input_workbook={"column3": [5, 6], "column4": [7, 8]}),
        DataExtractorOutputDict(processed_data={"key2": "value2"}),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_cases)
def test_data_extractor(input_data: DataExtractorInputDict, expected_output: DataExtractorOutputDict):
    # Create a DataExtractor instance
    data_extractor = DataExtractor()

    # Check if the component's configuration parameters have been set correctly
    assert data_extractor.data_processing_method is not None
    assert data_extractor.data_extraction_config_path is not None

    # Call the component's transform() method with the mocked input data
    output_data = data_extractor.transform(input_data)

    # Assert that the returned output data matches the expected output data
    assert output_data == expected_output

    # Add any error handling or edge case scenarios, if applicable
    # For example, you could test empty input_workbook or invalid data_processing_method values
