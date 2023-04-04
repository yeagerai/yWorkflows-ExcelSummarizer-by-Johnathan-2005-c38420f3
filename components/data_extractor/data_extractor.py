
import os
import yaml
import pandas as pd

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.abstract_component import AbstractComponent


class DataExtractorInputDict(BaseModel):
    input_workbook: dict


class DataExtractorOutputDict(BaseModel):
    processed_data: dict


class DataExtractor(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

        self.data_processing_method: str = yaml_data["parameters"]["data_processing_method"]
        self.data_extraction_config_path: str = yaml_data["parameters"]["data_extraction_config"]

    def transform(
        self, args: DataExtractorInputDict
    ) -> DataExtractorOutputDict:
        with open(self.data_extraction_config_path, "r", encoding="utf-8") as file:
            data_extraction_config = yaml.safe_load(file)

        input_workbook = args.input_workbook
        data_frame = pd.DataFrame(input_workbook)

        if self.data_processing_method == 'excel_apis':
            # Process data using Excel APIs
            pass
        elif self.data_processing_method == 'pandas':
            # Process data using pandas
            pass

        # Identify and extract relevant data patterns, trends, and anomalies
        processed_data = {}  # Update processed_data with the results

        out = DataExtractorOutputDict(
            processed_data=processed_data
        )
        return out


load_dotenv()
data_extractor_app = FastAPI()


@data_extractor_app.post("/transform/")
async def transform(
    args: DataExtractorInputDict,
) -> DataExtractorOutputDict:
    data_extractor = DataExtractor()
    return data_extractor.transform(args)

