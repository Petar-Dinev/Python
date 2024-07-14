# class Profile:
#     def __init__(self, username: str, password: str):
#         self.__username = self.set_username(username)
#         self.__password = self.set_password(password)
#
#     @staticmethod
#     def set_username(username) -> str:
#         if 5 <= len(username) <= 15:
#             return username
#         raise ValueError("The username must be between 5 and 15 characters.")
#
#     @staticmethod
#     def set_password(password) -> str:
#         have_digit = False
#         have_one_upper_letter = False
#         for ch in password:
#             if ch.isdigit():
#                 have_digit = True
#             if ch.isupper():
#                 have_one_upper_letter = True
#         if len(password) >= 8 and have_digit and have_one_upper_letter:
#             return password
#         raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#
#     def __str__(self):
#         return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username) -> None:
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password) -> None:
        have_digit = False
        have_one_upper_letter = False
        for ch in password:
            if ch.isdigit():
                have_digit = True
            if ch.isupper():
                have_one_upper_letter = True
        if len(password) >= 8 and have_digit and have_one_upper_letter:
            self.__password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


# test code:
# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
