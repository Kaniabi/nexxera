
_DB_USERS = []


def ping():
    return 'pong'


def delete_users():
    _DB_USERS.clear()


def post_users(body):
    from .schema import NixUser

    user = NixUser(body)
    _DB_USERS.append(user)
    user.id = len(_DB_USERS)
    return user.to_native(), 201


def get_users():
    return [i.to_native() for i in _DB_USERS]


def get_user(uid):
    for i_user in _DB_USERS:
        if i_user.id == uid:
            return i_user.to_native()
    return []  # TODO: Not found error.


def get_transactions():
    return 'GET transactions'


def get_transaction(tid):
    return f'GET transation: {tid}'


def post_transaction(message):
    return 'POST transaction'


