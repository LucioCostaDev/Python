
print("Comparação de Números")
print("Digite dois números")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"{numero1} e maior que numero {numero2}")
elif numero1 < numero2:
    print(f"{numero1} e menor que numero {numero2}")
else:
    print("Os dois números são iguais")