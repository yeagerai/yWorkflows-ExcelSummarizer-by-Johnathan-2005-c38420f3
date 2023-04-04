
import pytest
from pydantic import ValidationError
from summary_generator import SummaryGenerator, SummaryGeneratorInputDict, SummaryGeneratorOutputDict

# Define test cases with mocked input and expected output data
test_data = [
    (
        SummaryGeneratorInputDict(DataExtractor_output=["Lorem ipsum dolor sit amet"]),
        SummaryGeneratorOutputDict(summary="A mock summary for lorem ipsum with visual aids")
    ),
    (
        SummaryGeneratorInputDict(DataExtractor_output=["Another test text input"]),
        SummaryGeneratorOutputDict(summary="A mock summary for another test text input with visual aids")
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("mocked_input, expected_output", test_data)
def test_summary_generator_transform(mocked_input, expected_output):
    """Test the SummaryGenerator's transform() method and assert whether the output matches the expected output."""
    summary_generator = SummaryGenerator()
    
    # Call the component's transform() method with mocked input
    result = summary_generator.transform(mocked_input)

    # Assert that the output matches the expected output
    assert result == expected_output

# Test edge cases where input data might be invalid or empty
def test_summary_generator_with_invalid_input():
    """Test the SummaryGenerator's transform() method with invalid input data."""

    invalid_input = {"invalid_key": "invalid_value"}

    with pytest.raises(ValidationError):
        summary_generator_input = SummaryGeneratorInputDict(**invalid_input)
        summary_generator = SummaryGenerator()
        summary_generator.transform(summary_generator_input)

def test_summary_generator_with_empty_data():
    """Test the SummaryGenerator's transform() method with an empty list as input."""
    
    empty_input = SummaryGeneratorInputDict(DataExtractor_output=[])
    expected_output = SummaryGeneratorOutputDict(summary="An appropriate response for empty input with visual aids")
    
    summary_generator = SummaryGenerator()
    result = summary_generator.transform(empty_input)

    assert result == expected_output
