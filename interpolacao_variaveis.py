nome = "Débora"
idade = 27
profissao = "Programador"
linguagem = "Python"
saldo = 45.435
dados = {"nome": "Gulherme", "idade": 28}

print("Nome: %s idade: %d" % (nome, idade))
print("Nome: {} idade: {}".format(nome, idade))
print("Nome: {1} idade: {0}".format(idade, nome))
print("Nome: {1} idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} idade: {idade}".format(nome=nome, idade=idade))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} idade: {idade} saldo: {saldo:.2f}")