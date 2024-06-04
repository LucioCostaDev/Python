# nome=input("Digite seu Nome: " )
# print("Nome:", nome)

# s='python'
# i=4
# f=4.5
# b=True
# t=1,2,3
# l=[1,2,3,]
# c={1,2,3}
# d={"one":"um","two":"dois"}

# print(type(s))
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(t))
# print(type(l))
# print(type(c))
# print(type(d))

# x="python"
# print(type(x))
# x=123
# print(type(x))

# input("Qual seu nome:") recebe a varival para ser armazenada

# print("Lucio: ")

# nome = input("Digite seu nome: ")
# print("Seu nome e:", nome)

# pi=3.1415
# print(f'Valor de pi aproximado é {pi:.3f}')
# {dig=1.234567}
# print=(f'O número é {0}')
# print=(f'O número é {number}')5
# print=(f'O número é {dig:.2f}')
# print=(f'O número é {dig:.1f}')
# print=('O número é {dig:.1f}')

# Estruturas de Repetição
print ("#############################################################")
print("Olá seja bem vindo")
nome = input("Qual seu nome:")
print("Olá %s seja bem vindo!" % (nome))
print("Precisamos de mais dados você quer continuar? S(sim) ou N(náo)")
resp1 = input("Qual sua resposta? ")
if resp1 == "s":
    print("Seguiremos para o cadastro.")
elif resp1 == "n":
    print("Obrigado até a proxima!")
else:
    print("Resposta inválida. tente novamente.")
idade = input("Qual sua idade:")
if idade >= "18":
    print("Voce e de maior")
else:
    print("Voce e de Menor, precisa de um resposavél")
ident = input("Digite seu numero de identidade: ")
cpf = input("Digite seu numero de CPF: ")
print(f"Seu nome:{nome}, Identidade: {ident}, CPF: {cpf}, esta de acordo ou quer alterar? S-sim ou N-não")
if resp1 == "s":
    print("Vamos fazer algumas perguntas")
else:
    print("Vamos retorna para alterar")




