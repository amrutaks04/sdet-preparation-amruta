import pytest
@pytest.fixture
def valid_email_format():
    return ["amruta.ks2022cse@sece.ac.in","abc123@gmail.com","first.last@cyware.com",
            "akshay_123+@amazon.in"
    ]
@pytest.fixture
def invalid_email_format():
    return [
        "amruta.ks@.com","@gmail.com","$a@gmail.com","user@gmail..com"
    ]