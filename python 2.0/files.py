# Manipulação de dados
# open("Teste.txt", "X")
# R = Read
# W = Write
# X = Execute
# A = Append
# R+
# WB5

# arquivo = open("Teste.txt", "x")

# arquivo = open("números.txt", "w" )
# for linha in range (1, 100):
#     arquivo.write(f"{linha}\n")
# arquivo.close()

# conteudo = open("arquivo.txt", "a")
# conteudo.write("Uma linha qualquer\n")
# conteudo.write("Uma segunda linha qualquer\n")
# conteudo.write("Uma terceira linha qualquer\n")
# print(conteudo.read())

#  ler arquivos da internet
import requests
ler = requests.get("https://pt.wikipedia.org/wiki/Revolta_Paulista_de_1924")
print(ler)
# 
# r = requests.get("")
# print(r) 