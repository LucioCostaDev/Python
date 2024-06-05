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
# print ("#############################################################")
# print("Olá seja bem vindo")
# nome = input("Qual seu nome:")
# print("Olá %s seja bem vindo!" % (nome))
# print("Precisamos de mais dados você quer continuar? S(sim) ou N(náo)")
# resp1 = input("Qual sua resposta? ")
# if resp1 == "s":
#     print("Seguiremos para o cadastro.")
# elif resp1 == "n":
#     print("Obrigado até a proxima!")
# else:
#     print("Resposta inválida. tente novamente.")
# idade = input("Qual sua idade:")
# if idade >= "18":
#     print("Você e maior de idade")
# else:
#     print("Você e Menor de idade, precisa de um resposavél")
# ident = input("Digite seu numero de identidade: ")
# cpf = input("Digite seu numero de CPF: ")
# print(f"Seu nome:{nome}, Identidade: {ident}, CPF: {cpf}, esta de acordo ou quer alterar? S-sim ou N-não")
# if resp1 == "s":
#     print("Vamos continuar")
# else:
#     print("Vamos retorna para alterar")

# # ############################################# EXERCICIOS ###################################################
# # Elaborar um progrma Python para somar dois números 
# # somar dois numeros inteiros 
# # Entrada dos dados 
# n1 = int(input("Digite um primeiro número: "))
# n2 = int(input("Digite um segundo número: "))
# # processamento dos dados
# soma = n1 + n2
# # Impressão do resultado
# print("Soma:", soma) 

# # Elaborar um programa Python para somar os digitos de uma número menor que 100.
# # Somar os dígitos de um número menor que 100 
# numero = int(input("Digite um numero menor que 100: "))
# if numero >= 100:
#     print("O número deve ser menor que 100.")
# else:
#     dezena = numero // 10 # declaração de uma variavel em dezena, realizando uma divisão inteira // ignora a parte fracionaria do resultado
#     unidade = numero % 10 # declaração de uma unidade, realizando uma divisão de resto de um numero
#     soma = dezena + unidade # declaração no qual vai ser realizado a soma 
#     print("Soma: ", soma)

# Elaborar um programa Python para imprimir os divisores de uma número.
# Calcular os divisores de um número 
n = int(input("digite um número: "))
print("Os divisores de", n, "são:")
for i in range(1, n + 1):
    if n % i ==0:
        print(i,end=" ")




