# contador = int(input("Digite o número a ser contado: "))
# descontador = int(input("Digite o número a ser descontado: "))
# quantidadenumero = int(input("Digite o numero total de Ações: "))

# if contador <= quantidadenumero:
#     while contador <= quantidadenumero:
#         print(contador)
#         print("Contador")
#         contador += 1
        
# elif descontador >= quantidadenumero:
#     while descontador >= quantidadenumero:
#         print(descontador)
#         print("Descontando")
#         descontador -= 1
        
# else:
#     print("Valores não batem")

# (10, 0, -1) decrementando em for R: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# (0, 11, 1) contador em for R: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# for i in range (0, 11, 1):
#     print(i)

for i in range (1, 10, 1):
    for m in range (1, 10, 1):
        resultado = i * m
        print(f"{i} x {m} = {resultado}")
        