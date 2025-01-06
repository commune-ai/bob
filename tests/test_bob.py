
import pytest
from bob import Build

def test_build_initialization():
    builder = Build()
    assert builder is not None
    assert builder.anchor == 'OUTPUT'
    assert builder.endpoints == ["build"]

def test_process_text():
    builder = Build()
    test_text = "Simple text without special commands"
    processed_text = builder.process_text(test_text)
    assert processed_text == test_text

def test_build_simple():
    builder = Build()
    result = builder.build("Create a simple Python function", simple=True)
    assert isinstance(result, (str, dict))

if __name__ == '__main__':
    pytest.main([__file__])
