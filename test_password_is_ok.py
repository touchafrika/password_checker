import pytest
import re
from password_checker import password_is_ok
def test_password_is_ok():
    with pytest.raises(Exception):
        assert password_is_ok("") == Exception("Password is not OK if it is empty")

    with pytest.raises(Exception):
        assert password_is_ok("molash") == Exception("Password is not OK if its less than 8 characters")

    with pytest.raises(Exception):
        assert password_is_ok("jjjjjjjjjjj") == Exception
        assert password_is_ok("JJJJJJJJJJJ") == Exception
        assert password_is_ok("16161616161") == Exception
        assert password_is_ok("!@#$$%^&*()") == Exception
        assert password_is_ok("ttttttttttt") == Exception
        assert password_is_ok("tTttttttttt") == Exception
        assert password_is_ok("jjjJjjjjjj@1") == Exception

    assert password_is_ok("madk@tcjf") == True