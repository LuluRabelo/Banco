from datetime import datetime
from decimal import Decimal

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.pf = cpf

class Transacao:
    def __init__(self, tipo, valor):
        pass

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = Decimal('0.00')
        self.historico = []

    def depositar(self, valor):
        valor = Decimal(str(valor))

        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        transacao = Transacao("Depósito", valor)
        self.historico.append(transacao)