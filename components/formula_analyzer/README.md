
# FormulaAnalyzer

Analyzes all formulas used in the workbook and generates a detailed report on their purpose and function, using openpyxl, pandas, and custom-built formula parser and analyzer.

## Initial generation prompt
description: Analyzes all formulas used in the workbook and generates a detailed report
  on their purpose and function, using openpyxl, pandas, and custom-built formula
  parser and analyzer.
inputs_from_nodes: ExcelWorkbookReader output
name: FormulaAnalyzer


## Transformer breakdown
- Load the workbook using openpyxl
- Parse the formulas in the workbook using the specified parser (custom or openpyxl)
- Analyze the parsed formulas using the custom analyzer
- Aggregate analysis results and generate a report in pandas DataFrame format
- Return the FormulaAnalysisReport DataFrame

## Parameters
[{'name': 'formula_parser', 'default_value': 'custom', 'description': "The type of formula parser to use, either 'custom' or 'openpyxl'.", 'type': 'string'}, {'name': 'analyzer_settings', 'default_value': '{}', 'description': 'Configuration settings for the formula analyzer.', 'type': 'dict'}]

        