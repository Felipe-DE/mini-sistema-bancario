class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    # Getters e setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome.strip():
            self.__nome = novo_nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        self.__data_nascimento = nova_data

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self.__cpf = novo_cpf

    @property
    def identidade(self):
        return self.__identidade

    @identidade.setter
    def identidade(self, nova_identidade):
        self.__identidade = nova_identidade
