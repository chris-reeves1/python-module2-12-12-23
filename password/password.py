'''
module doc string
'''
class PasswordChecker:
    '''
    class doc string
    '''
    def __init__(self, password):
        """
        Constructor method that takes a password and initializes instance variables.
        """
        self.password = password

    def get_password_rating(self):
        """
        Method that returns a string indicating the rating of the password.
        """
        # Check for uppercase letters, lowercase letters, numbers, and special characters
        has_upper = False
        has_lower = False
        has_number = False
        has_special = False
        for char in self.password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isnumeric():
                has_number = True
            elif not char.isalnum():
                has_special = True
        # Check against common passwords
        common_passwords = [
            "password", "123456", "qwerty", 
            "abc123", "letmein", "monkey", "password1", 
            "12345678", "admin", "welcome", "Password1!"
            ]
        if self.password in common_passwords:
            return "Very weak"
        # check strength
        if len(self.password) < 8:
            return "Weak"
        elif len(self.password) < 12 and (not has_upper or not has_lower or not has_number):
            return "Moderate"
        elif len(self.password) < 12 and has_upper and has_lower and has_number:
            return "Strong"
        elif len(self.password) < 16 and has_upper and has_lower and has_number and has_special:
            return "Strong"
        elif len(self.password) >= 16:
            return "Very strong"
        else:
            return "Moderate"


history = {}

while True:
    password_check = input("Enter a password: ")

    if password_check in history:
        print(f"Password rating: {history[password_check][-1]}")
    else:
        checker = PasswordChecker(password_check)
        RATING = checker.get_password_rating()

        if password_check not in history:
            history[password_check] = []
        history[password_check].append(RATING)

        print(f"Password rating: {RATING}")
    print("History:")
    for password_check, ratings in history.items():
        print(f"Password: {password_check}")
        for rating in ratings:
            print(f" - Rating: {rating}")
    answer = input("Enter another password? (y/n): ")
    if answer.lower() != "y":
        break