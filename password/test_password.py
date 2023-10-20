from password_for_testing import PasswordChecker

def test_very_weak_password():
    checker = PasswordChecker()
    rating = checker.get_password_rating("password")
    assert rating == "Very weak"

def test_weak_password():
    checker = PasswordChecker()
    rating = checker.get_password_rating("password1")
    assert rating == "Very weak"

def test_moderate_password():
    checker = PasswordChecker()
    rating = checker.get_password_rating("Password1")
    assert rating == "Strong"

def test_strong_password():
    checker = PasswordChecker()
    rating = checker.get_password_rating("Password1!")
    assert rating == "Strong"

def test_very_strong_password():
    checker = PasswordChecker()
    rating = checker.get_password_rating("Password123!$%^&*")
    assert rating == "Very strong"