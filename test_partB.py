import pytest
from verify_email import validate_email

@pytest.mark.smoke
def testValid():
    assert validate_email("abc@gmail.com")

@pytest.mark.regression
def testInvalid():
    assert validate_email("abc$.vom")==False

@pytest.mark.readonlt
def testRead():
    assert validate_email("abc123@gmail.com")