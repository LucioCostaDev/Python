# nome = input ("DIgite seu nome: ")
# nascimento = input("Qual seu ano de nascimento? ")
# email = input("Digite seu email: ")
# print("Nome: ", nome , ". E-mail: " , email , ". Nascimento: ", nascimento)
# print(nome)
# print("Nascimento: ")
# print(nascimento)
# print("Email: ")
# print (email)
# num1 = input ("digite um número: ") 
# num2 = input ("digite um número: ") 
# num3 = input ("digite um número: ") 
# num4 = input ("digite um número: ")
# print("=> ", num1 , "=> ", num2, "=> ", num3, "=> ", num4)

# a = int(input("Digite um número: "))
# print (a + 5)

# int(input("Texto"))

# #Colocando varivel parta realizar calculo
# print (2*3) #multiplicação
# print (2**3) #potenciação
# print (2-3) #subtração
# print (2+3) #soma
# print (2/3) #divisão 

# #colocando uma variavel declarada
# a = 2
# b = 3
# print(a+b)

# from cmath import sqrt
# print(sqrt(4))

# nome = input("Digite seu nome: ")
# nascimento = input("Qual seu ano de nascimento: ")
# email = input("Qual seu email: ")
# print("Nome:",nome,".E-mail:",email,".Nascimento:",nascimento,".")

# idade = int(input("Digite sua idade: "))
# if idade > 18:
#     print("É maior de idade")
# elif idade == 18:
#     print("É guerreiro Jedi")
# else:
#     print("É menor de idade")

# TERNARIOS

# # VALOR FIXO 
# idade = 18
# print("É maior de idade") if idade >= 18 else print("É menor")

# # ATRIBUINDO VALOR
# idade = int(input("Digite uma idade:"))
# print("É maior de idade") if idade >= 18 else print("É menor")

# SWITCH CASE  NO PYTHON E (CASE MATCH)

# a = "Marcio"
# match a:
#     case "Antonio":
#         print("Não é Marcio")
#     case "Pedro":
#         print("É Pedro e não Marcio")
#     case "Marcio":
#         # print("Achou o Marcio")
#         sobrenome = input("Digite seu sobrenome")

# Um algoritmo que:
# peça ao usuário o para digitar o seu ano de nascimento
# peça o ano atual
# descubra se o usuário e maior de idade
# se for, pede o titulo de eleitor dele
# senão, pede um documento do responsavel.

# print("#####################################################")
# nasc = int(input("Digite seu ano de nascimento: "))
# anoatual = int(input("Digite o ano atual: "))
# idade = (anoatual-nasc)
# if idade >= 16:
#     print("Porfavor apresente o título")
# else:
#     print("Porfavor apresente um documento do responsavel")
# print("#####################################################")

# #While  = Laço de repetição enquanto

# a = 1

# while a <= 10:
#     print("teste")
#     a = a + 1

# FOR 

# a =["Lucio", "Pedro", "Luciano", "Alinne"]
# for a in a:
#     print(a)

# a = "Descomplica"

# for a in a:
#     print (a)

# Manipulação de lista 
# a = [] # criação de uma variavel tipo lista vazia
# b = 1  # vou dado um valor a variavel b
# print(a)
# while b <= 3:
#     a.append(input("Digite um nome de Aluno: "))
#     b = b + 1
# print(a) #append eu vou adicionar um noveo item ao final da minha lista

# # Metodo Insert e remove
# a = ["Marcio", "Bruna"]
# a.insert(1, "Hellen")
# print(a)
# a.remove("Marcio")
# print(a)

# DESENVOLVER ALGORTIMO: 
# Diretor cadastra alunos com dados:
# Nome, CPF, Email, Matricula.
# Para cada aluno castrado, o diretor pode lançar 3 notas
# Se a mmédia atingida for maior ou igual a 6, escrever: 
# Aluno X, voce foi aprovado. Seu diploma terá os seguintes dados:
# listar todos os dados daquele aluno
# Caso a média seja inferior a 6, lançar um nota adicional