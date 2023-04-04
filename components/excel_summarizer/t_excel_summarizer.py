
import pytest
import typing
from typing import Optional
from pydantic import BaseModel
from fastapi.testclient import TestClient
from .your_module_with_component import (
    excel_summarizer_app,
    ExcelWorkbookInput,
    WordDocumentOutput,
)

client = TestClient(excel_summarizer_app)


@pytest.mark.parametrize(
    "input_data, expected_output_data",
    [
        pytest.param(
            ExcelWorkbookInput(workbook_file=b"Excel data"),
            WordDocumentOutput(document_file=b"Word data"),
            id="normal_input",
        ),
        pytest.param(
            ExcelWorkbookInput(workbook_file=b""),
            WordDocumentOutput(document_file=b""),
            id="empty_input",
        ),
        pytest.param(
            ExcelWorkbookInput(workbook_file=b"Excel data with edge cases"),
            WordDocumentOutput(document_file=b"Word data with edge cases results"),
            id="edge_cases",
        ),
    ],
)
def test_component_transform(input_data: ExcelWorkbookInput, expected_output_data: WordDocumentOutput) -> None:
    response = client.post("/transform/", data=input_data.dict())

    assert response.status_code == 200
    assert response.json() == expected_output_data.dict()


def test_component_transform_error_handling() -> None:
    response = client.post("/transform/", data={"invalid_key": "Invalid value"})

    assert response.status_code == 422
    assert "detail" in response.json()
