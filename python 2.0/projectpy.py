# # PythonFlix
# nome = "Matrix"
# ano_lancamento = 2024
# nota_filme = 10.0
# plano = False

# # print(type(nome))
# # print(type(ano_lancamento))
# # print(type(nota_filme))
# # print(type(plano))

# # filme = input("Digite um nome de filme: \n")

# # print(filme)

# print("O nome do:",nome, "\nO ano do lançamento:",ano_lancamento, "\nA nota do filme e:",nota_filme)

# Operadores

# num1 = int(input("Digite o primeiro numero\n"))
# num2 = int(input("Digite o segundo numero\n"))

# sum = num1 + num2
# sub = num1 - num2
# div = num1 / num2
# mult = num1 * num2
# mod = num1 % num2

# print(f"A soma e {sum}\n2A subtração e {sub}\nA divisão e {div}\nA multiplicação e {mult}\nE o resto e {mod}")

# # CASE SENSITIVE
# filme1 = "Matrix"
# filme2 = "matrix"
# print(filme1 == filme2)

# descFilmes = """\nMatrix filme de ficção que fez bastante sucesso"""

# print(descFilmes)

# # MULTIPLICAÇÃO DE STRINGS
# line = "*"
# print(line*60)
# print(descFilmes)

# # Procurar uma palavra dentro de um texto
# print("Matrix" in descFilmes)
# print("Filmes" in descFilmes)

Filme = "Homem Aranha"

# 1- buscar toda string a apartir da primeira posição
print(filme[0:])

# 2- buscar toda string até a última posição 
print(filme[:7])

# 3- buscar toda string da terceira até a última posição 
print(filme[2:])

"""
String[inicio:fim:passo]
indice começa na posição 0 | indice final - 1
passo - dertermina o incremento. Por padrão esse número é o 1.

"""

#  4-  Buscar toda a string de 2 em 2 caracteres
print(filme[::2])

# 5- Buscar toda a string nos índices ímpares
print(filme[1::2])

# 6- Inverter uma string de trás para frente
print(Filme[::-1])