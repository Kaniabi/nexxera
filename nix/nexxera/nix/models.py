from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class NixUser(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), serialized_name='nome')
    cnpj = Column(String(14))


class NixTransaction(Base):
    __tablename__ = 'transacao'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, serialized_name='usuario_id')
    user = relationship("NixUser", backref=backref("transactions", order_by=id))

    # Creditor Account
    creditor_name = Column(String(128), serialized_name='pagador_nome')
    creditor_bank = Column(String(3), serialized_name='pagador_banco')
    creditor_agency = Column(String(4), serialized_name='pagador_agencia')
    creditor_account = Column(String(6), serialized_name='pagador_conta')

    # Debtor Account
    debtor_name = Column(String(128), serialized_name='beneficiario_nome')
    debtor_bank = Column(String(3), serialized_name='beneficiario_banco')
    debtor_agency = Column(String(4), serialized_name='beneficiario_agencia')
    debtor_account = Column(String(6), serialized_name='beneficiario_conta')

    amount = Column(Float, serialized_name='valor')

    # TODO: choices=['CC', 'TED', 'DOC']
    type = Column(String(4), serialized_name='tipo')
