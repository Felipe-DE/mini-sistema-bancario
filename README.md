# Mini Sistema Bancário em Python 🏦

Este é um projeto acadêmico desenvolvido como parte da **trilha de capacitação do programa Softex PE**. Ele integra duas atividades:

1. **Classe Pessoa** com atributos privados (`cpf` e `identidade`) e métodos getters e setters.  
2. **Classe ContaBancaria** associada à Pessoa, com saldo privado, depósitos e saques, garantindo que o saldo nunca fique negativo.

O projeto tem foco em **Programação Orientada a Objetos (POO)**, principalmente **encapsulamento** e boas práticas de manipulação de dados.

---

## Funcionalidades

- **Pessoa**
  - Nome
  - Data de nascimento
  - CPF (privado, com validação)
  - Identidade (privado)
- **Conta Bancária**
  - Titular (Pessoa)
  - Saldo privado
  - Depósito
  - Saque
  - Saldo nunca negativo
- Uso completo de **encapsulamento**:
  - Atributos privados (`__saldo`, `__titular`, `__cpf`, `__identidade`)
  - Métodos getters e setters (`@property` e `@setter`) para acesso seguro

---

---

## Exemplo de Uso

```python
from pessoa import Pessoa
from conta_bancaria import ContaBancaria

# Criando uma pessoa
pessoa1 = Pessoa("Gabriel", "22/09/2000", "12345678901", "MG1234567")

# Criando conta bancária associada à pessoa
conta1 = ContaBancaria(titular=pessoa1, saldo=1000)

# Consultando saldo e dados da pessoa
print(f"Saldo inicial de {conta1.titular.nome}: R${conta1.saldo}")
print(f"CPF: {conta1.titular.cpf}")
print(f"Identidade: {conta1.titular.identidade}")

# Operações
conta1.depositar(500)
print(f"Saldo após depósito: R${conta1.saldo}")

conta1.sacar(200)
print(f"Saldo após saque: R${conta1.saldo}")

# Tentativa de definir saldo negativo
conta1.saldo = -100
print(f"Saldo após tentativa de definir negativo: R${conta1.saldo}")

# Alterando dados da pessoa via encapsulamento
conta1.titular.cpf = "98765432100"
conta1.titular.identidade = "SP7654321"
print(f"CPF atualizado: {conta1.titular.cpf}")
print(f"Identidade atualizada: {conta1.titular.identidade}")

Tecnologias Utilizadas

Python 3.x

Conceitos de Programação Orientada a Objetos (POO)

Encapsulamento

Classes e objetos

Métodos getters e setters com @property

Considerações Finais

Este projeto é para fins acadêmicos, desenvolvido como parte da trilha de capacitação do programa Softex PE.
Ele garante que os dados privados, como saldo e CPF, só possam ser acessados ou modificados de forma controlada e segura, integrando as duas atividades em um único projeto.
