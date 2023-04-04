
# SummaryGenerator

Generates a summary of the workbook, including key insights and relevant visual aids, using natural language processing or machine learning techniques, such as BERT or GPT-3.

## Initial generation prompt
description: Generates a summary of the workbook, including key insights and relevant
  visual aids, using natural language processing or machine learning techniques, such
  as BERT or GPT-3.
inputs_from_nodes: DataExtractor output
name: SummaryGenerator


## Transformer breakdown
- 1. Load and initialize the chosen NLP model (either GPT-3 or BERT) as specified by the model_type parameter
- 2. Preprocess the extracted data from the DataExtractor_output input
- 3. Feed the preprocessed data into the NLP model
- 4. Generate a summary based on the NLP model's output, limiting it to the specified summary_length
- 5. Include any relevant visual aids or graphs to support the summary
- 6. Return the generated summary as the output

## Parameters
[{'name': 'model_type', 'default_value': 'gpt3', 'description': "Specifies the NLP model to be used for generating the summary (options: 'gpt3' or 'bert')", 'type': 'string'}, {'name': 'summary_length', 'default_value': 150, 'description': 'The maximum length of the generated summary in words', 'type': 'integer'}]

        