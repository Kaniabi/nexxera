from datetime import time

from flask_sqlalchemy import BaseQuery


class ValidationError(BaseException):
    def __init__(self, **errors):
        super(ValidationError, self).__init__()
        self.errors = errors


def create_models(db):
    from sqlalchemy.orm import validates

    # import enum
    # class TransactionType(enum.Enum):
    #     CC = "CC"
    #     TED = "TED"
    #     DOC = "DOC"

    class QueryWithSoftDelete(BaseQuery):
        """
        This class provides an alternative query implementation with support for soft-deletion.

        Reference: https://blog.miguelgrinberg.com/post/implementing-the-soft-delete-pattern-with-flask-and-sqlalchemy
        """

        _with_deleted = False

        def __new__(cls, *args, **kwargs):
            obj = super(QueryWithSoftDelete, cls).__new__(cls)
            obj._with_deleted = kwargs.pop("_with_deleted", False)
            if len(args) > 0:
                super(QueryWithSoftDelete, obj).__init__(*args, **kwargs)
                return obj.filter_by(deleted=False) if not obj._with_deleted else obj
            return obj

        def __init__(self, *args, **kwargs):
            pass

        def with_deleted(self):
            return self.__class__(
                db.class_mapper(self._mapper_zero().class_),
                session=db.session(),
                _with_deleted=True,
            )

        def _get(self, *args, **kwargs):
            # this calls the original query.get function from the base class
            return super(QueryWithSoftDelete, self).get(*args, **kwargs)

        def get(self, *args, **kwargs):
            # the query.get method does not like it if there is a filter clause
            # pre-loaded, so we need to implement it using a workaround
            obj = self.with_deleted()._get(*args, **kwargs)
            return obj if obj is None or self._with_deleted or not obj.deleted else None

    class User(db.Model):
        __tablename__ = "users"

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128))
        cnpj = db.Column(db.String(14))

    class Transaction(db.Model):
        __tablename__ = "transactions"

        # The maximum amount accepted by a transaction.
        MAX_AMOUNT = 100000.00
        TED_MIN_AMOUNT = 5000.00
        TED_START_TIME = time(10)
        TED_END_TIME = time(16)

        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
        # user = db.relationship("User", backref=db.backref("transactions", lazy=True))

        # Creditor Account
        creditor_name = db.Column(db.String(128), nullable=False)
        creditor_bank = db.Column(db.String(3), nullable=False)
        creditor_agency = db.Column(db.String(4), nullable=False)
        creditor_account = db.Column(db.String(6), nullable=False)

        # Debtor Account
        debtor_name = db.Column(db.String(128), nullable=False)
        debtor_bank = db.Column(db.String(3), nullable=False)
        debtor_agency = db.Column(db.String(4), nullable=False)
        debtor_account = db.Column(db.String(6), nullable=False)

        amount = db.Column(db.Float)

        # TODO: Should be an enumerate of TransactionType
        type = db.Column(db.String(3))

        status = db.Column(db.String(12), default="OK")

        # Soft deletion
        query_class = QueryWithSoftDelete
        deleted = db.Column(db.Boolean, default=False)

        @validates("amount")
        def validate_amount(self, _key, value):
            """
            The amount must be lower than MAX_AMOUNT.
            """
            if value > self.MAX_AMOUNT:
                self.status = "ERRO"
            return value

        @classmethod
        def post_preprocessor(cls, data=None, **kw):
            """
            Automatically calculates the type attribute.
            """
            from datetime import datetime

            # TODO: Implement the correct timestamp, including the possibility to receiving it by paramter (for testing)
            timestamp = datetime(2019, 5, 6, 19, 0, 0)

            data["type"] = "DOC"
            if data["debtor_bank"] == data["creditor_bank"]:
                data["type"] = "CC"
            elif (
                data["amount"] < cls.TED_MIN_AMOUNT
                and cls.TED_START_TIME < timestamp.time() < cls.TED_END_TIME
            ):
                data["type"] = "TED"
            return data

        @classmethod
        def get_many_postprocessor(cls, result=None, search_params=None, **kw):
            """
            Adds total_amount to the GET MANY results.
            """
            total_amount = sum([i["amount"] for i in result["objects"]])
            result["total_amount"] = total_amount
            return result

    class Models:
        NixUser = User
        NixTransaction = Transaction

    return Models
