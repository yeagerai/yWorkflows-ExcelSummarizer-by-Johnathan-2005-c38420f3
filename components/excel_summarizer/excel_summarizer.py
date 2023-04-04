
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class ExcelWorkbookInput(BaseModel):
    workbook_file: bytes


class WordDocumentOutput(BaseModel):
    document_file: bytes


class ExcelSummarizer(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: ExcelWorkbookInput, callbacks: typing.Any
    ) -> WordDocumentOutput:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        document_file = results_dict[4].document_file
        out = WordDocumentOutput(document_file=document_file)
        return out

load_dotenv()
excel_summarizer_app = FastAPI()


@excel_summarizer_app.post("/transform/")
async def transform(
    args: ExcelWorkbookInput,
) -> WordDocumentOutput:
    excel_summarizer = ExcelSummarizer()
    return await excel_summarizer.transform(args, callbacks=None)

