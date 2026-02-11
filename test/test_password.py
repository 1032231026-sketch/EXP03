from password import check_password_strength

def test_weak():
    assert check_password_strength("abc") == "Weak"

def test_medium():
    assert check_password_strength("abcdef") == "Medium"

def test_strong():
    assert check_password_strength("Abc123") == "Strong"
