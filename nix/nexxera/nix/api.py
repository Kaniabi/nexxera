

_DB_USERS = []
_DB_TRANSACTIONS = []


def ping():
    return 'pong'


def delete_users():
    _DB_USERS.clear()


def post_users(body):
    from .schema import NixUser

    obj = NixUser(body)
    _DB_USERS.append(obj)
    obj.id = len(_DB_USERS)
    return obj.to_native(), 201


def get_users():
    return [i.to_native() for i in _DB_USERS]


def get_user(uid):
    for i_user in _DB_USERS:
        if i_user.id == uid:
            return i_user.to_native()
    return []  # TODO: Not found error.


def delete_transactions():
    _DB_TRANSACTIONS.clear()


def get_transactions():
    return [
        i.to_native()
        for i in _DB_TRANSACTIONS
        if not i.deleted
    ]


def get_transaction(tid):
    return ""


def post_transaction(body):
    from .schema import NixTransaction

    obj = NixTransaction(body)
    _DB_TRANSACTIONS.append(obj)
    obj.id = len(_DB_TRANSACTIONS)
    return obj.to_native(), 201


def delete_transaction(tid):
    obj = _get_transaction(tid)
    if obj is None:
        return '', 404

    for i, i_transaction in enumerate(_DB_TRANSACTIONS):
        if i_transaction.id == tid:
            i_transaction.deleted = True

    return '', 200


def _get_transaction(tid):
    for i_transaction in _DB_TRANSACTIONS:
        if i_transaction.id == tid:
            return i_transaction
    return None
