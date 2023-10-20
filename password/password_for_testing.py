class PasswordChecker:
    def __init__(self):
        """
        Constructor method that initializes instance variables.
        """
        pass

    def get_password_rating(self, password):
        """
        Method that takes a password and returns a string indicating the rating of the password.
        """
        # Check for uppercase letters, lowercase letters, numbers, and special characters
        has_upper = False
        has_lower = False
        has_number = False
        has_special = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isnumeric():
                has_number = True
            elif not char.isalnum():
                has_special = True
        
        # Check against list
        common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "monkey", "password1", "12345678", "admin", "welcome"]
        if password in common_passwords:
            return "Very weak"

        # check strength
        if len(password) < 8:
            return "Weak"
        elif len(password) < 12 and (not has_upper or not has_lower or not has_number):
            return "Moderate"
        elif len(password) < 12 and has_upper and has_lower and has_number:
            return "Strong"
        elif len(password) < 16 and has_upper and has_lower and has_number and has_special:
            return "Strong"
        elif len(password) >= 16:
            return "Very strong"
        else:
            return "Moderate"