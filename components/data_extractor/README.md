
# DataExtractor

Extracts and preprocesses relevant data from the input workbook, such as data trends, patterns, and anomalies, using Excel APIs, pandas or data sources. The component reads the input workbook data, processes it, identifies significant data points and trends, and outputs the processed data in a format suitable for further usage in the workflow.

## Initial generation prompt
description: Extracts and preprocesses relevant data from the input workbook, such
  as data trends, patterns, and anomalies, using Excel APIs, pandas or data sources.
inputs_from_nodes: ExcelWorkbookReader output
name: DataExtractor


## Transformer breakdown
- Load and parse the data_extraction_config YML file.
- Initialize the DataFrame with the input workbook data.
- Perform preprocessing based on the chosen data_processing_method (Excel APIs or pandas).
- Identify and extract relevant data patterns, trends, and anomalies.
- Return the processed data as output.

## Parameters
[{'name': 'data_processing_method', 'default_value': 'pandas', 'description': "The method used for data processing, available options are 'excel_apis' or 'pandas'", 'type': 'str'}, {'name': 'data_extraction_config', 'default_value': 'default_config.yml', 'description': 'Configuration file path specifying the data extraction rules and data preprocessing settings', 'type': 'str'}]

        