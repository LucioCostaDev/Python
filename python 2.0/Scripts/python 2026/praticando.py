# Vamos estudar de uma maneira pratica
print("Vamos estudar Python")
nome = input("Qual seu Mome? \n")
idade = int(input("Qual sua idade? \n"))
cpf = int(input("Qual seu CPF? \n"))
salario = int(input("Qual seu Salario? \n"))

print("Seus dados foram inseridos")

print("total de caracteres no nome são:")
print(len(nome))

if idade <= 17:
    print("Você e Menor de Idade")
else:
    print("Voce e Maior de Idade")

if salario <= 1621: 
    print(f"Seu salario de {salario:.2f} é menor que o minimo")
else:
    print(f"Seu salario de {salario:.2f} é maior que o minimo")

print("")