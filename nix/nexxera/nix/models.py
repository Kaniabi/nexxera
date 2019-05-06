def create_models(db):
    import enum

    class TransactionType(enum.Enum):
        CC = "CC"
        TED = "TED"
        DOC = "DOC"

    class User(db.Model):
        __tablename__ = "users"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128))
        cnpj = db.Column(db.String(14))

    class Transaction(db.Model):
        __tablename__ = "transactions"

        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        # user = db.relationship("User", backref=db.backref("transactions", lazy=True))

        # # Creditor Account
        # creditor_name = db.Column(db.String(128))
        # creditor_bank = db.Column(db.String(3))
        # creditor_agency = db.Column(db.String(4))
        # creditor_account = db.Column(db.String(6))
        #
        # # Debtor Account
        # debtor_name = db.Column(db.String(128))
        # debtor_bank = db.Column(db.String(3))
        # debtor_agency = db.Column(db.String(4))
        # debtor_account = db.Column(db.String(6))

        amount = db.Column(db.Float)

        # TODO: Should be an enumerate of TransactionType
        type = db.Column(db.String(3))

    class Models:
        NixUser = User
        NixTransaction = Transaction

    return Models
