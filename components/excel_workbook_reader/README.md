
# ExcelWorkbookReader

The ExcelWorkbookReader component is designed to read the input Excel workbook file and store its content and structure for further processing. It utilizes the openpyxl or pandas library to read the Excel file's contents and structure, allowing easy extraction of data from individual sheets or ranges within the workbook. This component can be used to load data from Excel files in a Yeager Workflow, where it can be combined with other components for processing or analysis.

## Initial generation prompt
description: Reads the input Excel workbook file and stores its content and structure
  for further processing, using openpyxl or pandas library.
name: ExcelWorkbookReader


## Transformer breakdown
- 1. Import the specified library (either 'openpyxl' or 'pandas')
- 2. Read the input Excel workbook file using the appropriate library function
- 3. Store the workbook data and structure in an object
- 4. Return the workbook_data object as the output

## Parameters
[{'name': 'library_choice', 'default_value': 'pandas', 'description': "The library to be used for reading the Excel workbook file, either 'openpyxl' or 'pandas'.", 'type': 'str'}]

        