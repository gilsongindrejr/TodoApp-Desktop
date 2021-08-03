def auth_user(name: str, db_name: str) -> int:
    """
    Authenticate username

    Parameters:
        name (str):The name that will be compared with the name stored in database.
        db_name (str):The username in database that will be compared with the username the user submitted.

    Returns:
        0(int):Username can be used.
        1(int):Username already in use.
    """
    try:
        if name == db_name[0][0]:
            return 1
        else:
            return 0
    except IndexError:
        return 0


def auth_pass_reg(password: str, password_c: str) -> int:
    """
    Authenticate password in register

    Parameters:
        password (str):The password that user submitted.
        password_c (str):The password confirmation that will be compared with the password the user submitted.

    Returns:
        0(int):Password match.
        1(int):Password doesn't match.
    """
    if password != password_c:
        return 1
    else:
        return 0


def auth_pass_log(password: str, db_password: str) -> int:
    """
    Authenticate password in login

    Parameters:
        password (str):The password that will be compared with the password stored in database.
        db_password (str):The password in database that will be compared with the password the user submitted.

    Returns:
        0(int):Correct password.
        1(int):Incorrect password.
    """
    try:
        if password == db_password[0][0]:
            return 1
        else:
            return 0
    except IndexError:
        return 0


def auth_email(email: str, db_email: str) -> int:
    """
    Authenticate email

    Parameters:
        email (str):The email that will be compared with the database email.
        db_email (str):The email in database that will be compared with the email the user submitted.

    Returns:
        0(int):Email can be used.
        1(int):Email already in use.
    """
    try:
        if email == db_email[0][0]:
            return 1
        else:
            return 0
    except IndexError:
        return 0
