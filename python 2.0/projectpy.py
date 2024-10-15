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

# filme = "Homem Aranha"

# # 1- buscar toda string a apartir da primeira posição
# print(filme[0:])

# # 2- buscar toda string até a última posição 
# print(filme[:7])

# # 3- buscar toda string da terceira até a última posição 
# print(filme[2:])

# """
# String[inicio:fim:passo]
# indice começa na posição 0 | indice final - 1
# passo - dertermina o incremento. Por padrão esse número é o 1.

# """

# #  4-  Buscar toda a string de 2 em 2 caracteres
# print(filme[::2])

# # 5- Buscar toda a string nos índices ímpares
# print(filme[1::2])

# # 6- Inverter uma string de trás para frente
# print(filme[::-1])

# movieName = "Homem Aranha"
# movieDescription = """
# Homen Aranha, e um filme de super heroi que ganho poder, através de uma picada de aranha"""

# print(movieName.upper()) # tudo maiusculo
# print(movieName.lower()) # tudo minusculo
# print(movieName.capitalize()) # Primeira Letra maiuscula
# print(movieName.title()) # Primeira Letra Maiuscula
# print(movieName.center(10, '-')) #Retorna string centralizada com caractere de preenchimento
# print(movieName.find("u")) # Retorna a posição de um determinado caractere
# print(movieName.find("o")) # conta caracteres
# print(movieName.replace("Homem", "Spider")) # troca caracteres
# print(movieDescription.split(',')) # coloca em uma estrutura python

# # Exercicios

# primeiroNome = input("Digite o nome:\n")
# segundoNome = input("Digite o sobrenome:\n")

# nomeFormatado = f"{primeiroNome} {segundoNome}"
# print(nomeFormatado)

# # Exerciocios2
# texto = "Python é muito interessante"
# palavras = texto.split()
# textoInvertido = " ".join(palavras[::-1])
# print(textoInvertido)

# #  exercio palindromo e quando a palavra e igual tanto lendo de frente para tras como de tras para frente
# texto1 = "arara"
# texto2 = "python"

# # aqui a formatação vai diminuir e tirar os espaços
# texto1_format = texto1.lower().replace(" ","")
# texto2_format = texto2.lower().replace(" ","")

# # verificar se texto original e igual ao seu reverso
# palindromo1 = texto1_format == texto1[::-1]
# palindromo2 = texto2_format == texto2[::-1]

# print(palindromo1)
# print(palindromo2)

# # LISTAS
# filmMatrix = ["Matrix", 1999, 8.7, True]
# print(filmMatrix)

# filmList = ["Star Wars", "Marvel", "Rei Leão", "Alladim"]

# # 1 - Buscar os dois primeiros itens da lista
# print(filmList[:2])

# # 2 - Buscar o último item da lista
# print(filmList[-1])

# # 3 - Buscar filmes até uma determinada posição

# print(filmList[:3])

# #  4 - Buscar filmes de uma posição em diante
# print(filmList[1:4])

filmList = ["Star Wars", "Marvel", "Rei Leão", "Alladim"]