contador = int(input("Digite o número a ser contado: "))
descontador = int(input("Digite o número a ser descontado: "))
quantidadenumero = int(input("Digite o numero total de Ações: "))

if contador <= quantidadenumero:
    while contador <= quantidadenumero:
        print(contador)
        contador += 1
        
elif descontador >= quantidadenumero:
    while descontador >= quantidadenumero:
        print(descontador)
        descontador -= 1
        
else:
    print("Valores não batem")
