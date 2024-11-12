# # Informações sobre Filme
# name = input("Digite o nome do filme:\n")
# yearRelease = int(input("Digite o ano de lançamento:\n"))
# rating = float(input("Digite a nota de avaliação do filme:\n"))

# #Verifivar se o fime é recomendado
# if rating > 8.0 and yearRelease > 2015:
#     print(f"O filme {name} é muito bom. Recomedo assisti-lo")
# else:
#     print(f"O filme {name} ainda não stigiu uma boa nota.")

# num1 = float(input("Digite o primeiro número:\n"))
# num2 = float(input("Digite o primeiro número:\n"))
# operation = input("Digite a operação a ser realizada: (+ - * /)\n")

# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2  
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         print("Erro: Divisão por zero")
#         result = 0

# else:
#     print("Operação inválida")
#     result = 0

# print(f"Resultado da operação é: {result:.2f}")

# FOR 
listadeFilmes = ["Matrix", "Titanic", "Star War", "Anjos da noite"]

# 1 - iterando valores de uma lista
for filmes in listadeFilmes:
    print(filmes)
    
# 2 - Quando a condição for atendida, o loop vai encerrar
for filmes in listadeFilmes:
    if filmes == "Star War":
        break
    print(filmes)

# 3 - Quando a condição for atendida, o loop vai para proxima iteração
for filmes in listadeFilmes:
    if filmes == "Star War":
        continue
    print(filmes)

# 4 - Avaliação do filme:
nomeFilme = input("Digite o nome do filme:\n")
notaFilme = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0 
for i in range(notaFilme):
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    
if notaFilme > 0:
    average = total / notaFilme
else:
    average = 0
    
print(f"Média de avaliação do filme {nomeFilme} é: {average:.2f}")