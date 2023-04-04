
import os

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent

# Define Input and Output Data Models
class SummaryGeneratorInputDict(BaseModel):
    DataExtractor_output: list

class SummaryGeneratorOutputDict(BaseModel):
    summary: str

class SummaryGenerator(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        
        # Load the configuration
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        
        self.model_type = yaml_data["parameters"]["model_type"]
        self.summary_length = yaml_data["parameters"]["summary_length"]

    def preprocess_data(self, data):
        # Preprocess the extracted data from DataExtractor_output input
        pass

    def generate_summary(self, data):
        # Generate a summary based on the NLP model's output, limiting it to the specified summary_length
        pass

    def include_visual_aids(self, data):
        # Include any relevant visual aids or graphs to support the summary
        pass

    def transform(self, args: SummaryGeneratorInputDict) -> SummaryGeneratorOutputDict:
        # Load and initialize the chosen NLP model (either GPT-3 or BERT) as specified by the model_type parameter
        pass

        # Preprocess the extracted data
        preprocessed_data = self.preprocess_data(args.DataExtractor_output)

        # Feed the preprocessed data into the NLP model
        pass

        # Generate the summary
        summary = self.generate_summary(preprocessed_data)

        # Include any relevant visual aids or graphs to support the summary
        summary_with_visual_aids = self.include_visual_aids(summary)

        # Return the generated summary as the output
        return SummaryGeneratorOutputDict(summary=summary_with_visual_aids)

# Load environment variables
load_dotenv()

# Create FastAPI app and endpoint
summary_generator_app = FastAPI()

@summary_generator_app.post("/transform/")
async def transform(args: SummaryGeneratorInputDict) -> SummaryGeneratorOutputDict:
    summary_generator = SummaryGenerator()
    return summary_generator.transform(args)
