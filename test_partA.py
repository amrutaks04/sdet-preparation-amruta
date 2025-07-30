import pytest
from verify_email import validate_email

class TestUserValidation:
    @pytest.mark.parametrize("Valid_email",
                             ["amruta.ks2022cse@sece.ac.in",
                            "abc123@gmail.com","first.last@cyware.com",
                            "akshay_123+@amazon.in"])
   
    def test_valid_email(self,Valid_email):
        assert validate_email(Valid_email)==True

    @pytest.mark.parametrize("Invalid_email",["amruta.ks@.com","@gmail.com",
                                              "$a@gmail.com","user@gmail..com"])
    
    def test_invalid_email(self,Invalid_email):
        assert validate_email(Invalid_email)==False
    



