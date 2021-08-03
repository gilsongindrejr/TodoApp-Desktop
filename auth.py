def auth_user(name, db_name):
    '''
    Authenticate username

    Args:
        name (str):The name that will be compared with the database name.
        db_name (str):The username in database that will be compared with the username the user submitted.

    Returns:
        0(int):Username can be used.
        1(int):Username already in use.
    '''
    try:
        if name == db_name[0][0]:
            return 1
        else:
            return 0
    except IndexError:
        return 0


def auth_pass(password, password_c):
    '''
    Authenticate password

    Parameters:
        password (str):The password that will be compared with the database password.
        password_c (str):The password confirmation that will be compared with the password the user submitted.

    Returns:
        0(int):Password match.
        1(int):Password doesn't match.
    '''
    if password != password_c:
        return 1
    else:
        return 0


def auth_email(email, db_email):
    '''
    Authenticate email

    Parameters:
        email (str):The email that will be compared with the database email.
        db_email (str):The email in database that will be compared with the email the user submitted.

    Returns:
        0(int):Email can be used.
        1(int):Email already in use.
    '''
    try:
        if email == db_email[0][0]:
            return 1
        else:
            return 0
    except IndexError:
        return 0
