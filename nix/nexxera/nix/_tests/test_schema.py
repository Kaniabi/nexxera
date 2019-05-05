

def test_smoke_user():
    from nexxera.nix.schema import NixUser
    user = NixUser(dict(name="Alpha", cnpj="123"))
    assert user.name == "Alpha"
    assert user.cnpj == "123"


def test_smoke_transaction():
    from nexxera.nix.schema import NixTransaction
    transaction = NixTransaction(dict(amount=100.0))
    assert transaction.amount == 100.0
