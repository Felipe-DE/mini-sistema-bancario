from pessoa import Pessoa
from conta_bancaria import ContaBancaria

# Criando uma pessoa
pessoa1 = Pessoa("Gabriel", "22/09/2000", "12345678901", "MG1234567")

# Criando conta bancária associada à pessoa
conta1 = ContaBancaria(titular=pessoa1, saldo=1000)

# Demonstração de uso integrado
print(f"Saldo inicial de {conta1.titular.nome}: R${conta1.saldo}")
print(f"CPF: {conta1.titular.cpf}")
print(f"Identidade: {conta1.titular.identidade}")

conta1.depositar(500)
print(f"Saldo após depósito: R${conta1.saldo}")

conta1.sacar(200)
print(f"Saldo após saque: R${conta1.saldo}")

# Tentativa de definir saldo negativo
conta1.saldo = -100
print(f"Saldo após tentativa de definir negativo: R${conta1.saldo}")

# Alterando dados da pessoa
conta1.titular.cpf = "98765432100"
conta1.titular.identidade = "SP7654321"
print(f"CPF atualizado: {conta1.titular.cpf}")
print(f"Identidade atualizada: {conta1.titular.identidade}")
