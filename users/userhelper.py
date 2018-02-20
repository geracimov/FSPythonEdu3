__logged_users__ = ()
__registered_users__ = {'admin': 'admin1'}


def log_user(login):
    for lu in __logged_users__:
        if lu == login:
            return True
    return False


def auth_user(login, pwd):
    return __registered_users__.get(login) == pwd


def register_user(login, pwd):
    if __registered_users__.get(login) is None:
        __registered_users__.update({login, pwd})
        return True
    return False
