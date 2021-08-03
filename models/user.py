class User:
    '''
    A class to represent a user.

    Attributes:
        name (str):User name.
        password (str):User password.
        password_c(int):Password confirmation.
        email(int):User email.

    Methods:
        Only constructor, getters and setters.
    '''
    def __init__(self, name, password, password_c, email):
        self.__name = name
        self.__password = password
        self.__password_c = password_c
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def password_c(self):
        return self.__password_c

    @password_c.setter
    def password_c(self, password_c):
        self.__password_c = password_c

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
