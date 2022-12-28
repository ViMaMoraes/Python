'''
nome = 'Andre'
nome_lower = nome.lower()

print(nome_lower)
'''


'''
class Funcionarios:
    nome = 'Elena'
    sobrenome = 'Cabral'
    data_nascimento = '12/01/2009'


usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
'''

# criar a classe




from datetime import datetime
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionarios(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005)
usuario3 = Funcionarios('Marcus', 'Moraes', 2000)

# print
# print(usuario1.nome_completo())
print(Funcionarios.idade_funcionarios(usuario1))
# print(usuario1.nome + ' ' + usuario1.sobrenome)
# print(usuario2.sobrenome)
# print(usuario3.data_nascimento)

'''
# criar parametros usuário1
usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
usuario1.data_nascimento = '12/01/2009'

# criar parametros usuário2
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '15/10/2005'
'''
