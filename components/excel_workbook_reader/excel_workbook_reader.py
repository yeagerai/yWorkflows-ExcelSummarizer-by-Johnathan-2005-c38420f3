
import os
from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import yaml
from pandas import read_excel
from openpyxl import load_workbook

from core.abstract_component import AbstractComponent

class ExcelWorkbookReaderInputDict(BaseModel):
    excel_file_path: str

class ExcelWorkbookReaderOutputDict(BaseModel):
    workbook_data: Any

class ExcelWorkbookReader(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.library_choice: str = yaml_data["parameters"]["library_choice"]

    def transform(self, args: ExcelWorkbookReaderInputDict) -> ExcelWorkbookReaderOutputDict:
        if self.library_choice == "openpyxl":
            workbook_data = load_workbook(args.excel_file_path)
        elif self.library_choice == "pandas":
            workbook_data = read_excel(args.excel_file_path, sheet_name=None)
        else:
            raise ValueError("Invalid library_choice specified in the configuration.")

        return ExcelWorkbookReaderOutputDict(workbook_data=workbook_data)

load_dotenv()
excel_workbook_reader_app = FastAPI()

@excel_workbook_reader_app.post("/transform/")
async def transform(args: ExcelWorkbookReaderInputDict) -> ExcelWorkbookReaderOutputDict:
    excel_workbook_reader = ExcelWorkbookReader()
    return excel_workbook_reader.transform(args)
