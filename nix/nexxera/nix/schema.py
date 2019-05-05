from schematics.models import Model
from schematics.types import StringType, DecimalType, IntType, BooleanType


class NixUser(Model):
    id = IntType()
    name = StringType(serialized_name='nome', max_length=128)
    cnpj = StringType(max_length=14)


class NixTransaction(Model):
    id = IntType()
    user_id = IntType(serialized_name='usuario_id')

    # # Creditor Account
    # creditor_name = StringType(serialized_name='pagador_nome', max_length=128)
    # creditor_bank = StringType(serialized_name='pagador_banco', max_length=3)
    # creditor_agency = StringType(serialized_name='pagador_agencia', max_length=4)
    # creditor_account = StringType(serialized_name='pagador_conta', max_length=6)
    #
    # # Debtor Acccount
    # debtor_name = StringType(serialized_name='beneficiario_nome', max_length=128)
    # debtor_bank = StringType(serialized_name='beneficiario_banco', max_length=3)
    # debtor_agency = StringType(serialized_name='beneficiario_agencia', max_length=4)
    # debtor_account = StringType(serialized_name='beneficiario_conta', max_length=6)

    amount = DecimalType(serialized_name='valor')
    # type = StringType(serialized_name='tipo', max_length=4, choices=['CC', 'TED', 'DOC'])

    deleted = BooleanType(default=False)
