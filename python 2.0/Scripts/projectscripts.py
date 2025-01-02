############ SCRIPT INICIAÇÃO ###################

# import pyautogui as posicaoMouse

# posicaoMouse.sleep(6) 

# # print(posicaoMouse.position()) tem como objetivo pega a posição de que mouse fica por isso definir o tempo para que possa após da run e tempo que o ponteiro do mouse fica seja capitado

# posicaoMouse.moveTo(x=561, y=1055) #posição menu windows
# posicaoMouse.click(x=561, y=1055)

# # posicaoMouse.sleep(2)
# # posicaoMouse.typewrite('excel')

# posicaoMouse.sleep(4) # e o tempo de espera do computador pensar
# # print(posicaoMouse.position())
# posicaoMouse.typewrite('cal')
# posicaoMouse.sleep(4)
# posicaoMouse.moveTo(x=659, y=495) #posição menu calculadora
# posicaoMouse.click(x=659, y=495)

############ SCRIPT VERIFICAR DOLAR ###################

# import pyautogui as posicaoAbrirGoogle

# posicaoAbrirGoogle.sleep(4)

# # print(posicaoAbrirGoogle.position()) apenas para pegar a posição 

# posicaoAbrirGoogle.click(x=1179, y=1063)
# posicaoAbrirGoogle.sleep(3)
# posicaoAbrirGoogle.typewrite('www.google.com.br')
# posicaoAbrirGoogle.sleep(2)
# posicaoAbrirGoogle.press('enter')
# posicaoAbrirGoogle.sleep(2)
# posicaoAbrirGoogle.typewrite('dolar hoje')
# posicaoAbrirGoogle.sleep(2)
# posicaoAbrirGoogle.press('enter')

############ SCRIPT ABRIR ARQUIVO ###################

# import pyautogui as posicaoAbreArquivos

# # O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
# # Nesse caso é a mesma coisa que precionar Windows + R 
# posicaoAbreArquivos.hotkey('win', 'r')

# # tempo de esperar para processar 
# posicaoAbreArquivos.sleep(2)

# # Digitamos a palavra Notpad
# posicaoAbreArquivos.typewrite('notepad')

# posicaoAbreArquivos.sleep(2)

# # Apertamos a tecla enter
# posicaoAbreArquivos.press('enter')

# posicaoAbreArquivos.sleep(6)

# posicaoAbreArquivos.typewrite('Abrimos o notepaddddddd ')

# posicaoAbreArquivos.sleep(3)

# # O getAcitve Windows pega a janela ativa
# fecharJanela = posicaoAbreArquivos.getActiveWindow()

# posicaoAbreArquivos.sleep(2)    

# #aciona para fecha a janela ativa
# fecharJanela.close()

# posicaoAbreArquivos.sleep(2)

# posicaoAbreArquivos.press('tab')

# posicaoAbreArquivos.sleep(2)

# posicaoAbreArquivos.press('enter')

################## SCRIPT COM ESCOLHAS #######################

import pyautogui
import pyautogui as escolhas_opacao

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Excel', 'Word', "Notepad"])

if opcao == "Excel":
    
    # O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    # Nesse caso é a mesma coisa que precionar Windows + R 
    escolhas_opacao.hotkey('win', 'r')
    # tempo de esperar para processar 
    escolhas_opacao.sleep(3)
    # Digitamos a palavra excel
    escolhas_opacao.write('excel')
    # Apertamos a tecla enter
    escolhas_opacao.press('enter')
    # tempo de esperar para processar 
    escolhas_opacao.sleep(3)
    # pega a posição 
    # print(escolhas_opacao.position())
    #clica na posição 
    escolhas_opacao.click(x=269, y=213)
    escolhas_opacao.write('Escolhi o Excel')
    
elif opcao == "Word":
    # O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    # Nesse caso é a mesma coisa que precionar Windows + R 
    escolhas_opacao.hotkey('win')
    # Digitamos a palavra Word
    escolhas_opacao.write('word')
    # tempo de
    # esperar para processar
    escolhas_opacao.sleep(3)
    # pega posição
    # print(escolhas_opacao.position())
    escolhas_opacao.click(x=653, y=482)
    # Apertamos a tecla enter
    escolhas_opacao.press('enter')
    # tempo para processar processar tarefa(linha)
    escolhas_opacao.sleep(3)
    # # pega posição
    # print(escolhas_opacao.position())
    escolhas_opacao.click(x=1315, y=1063)
    # tempo de processamento
    escolhas_opacao.sleep(4)
    # pega posição 
    # print(escolhas_opacao.position())
    # pressionar a posição
    escolhas_opacao.click(x=447, y=376)
    # tempo de espera
    escolhas_opacao.sleep(3)
    # escrever no programa
    escolhas_opacao.write('Escolhi o Word')    
elif opcao == "Notepad":
     # O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    # Nesse caso é a mesma coisa que precionar Windows + R 
    escolhas_opacao.hotkey('win', 'r')
    escolhas_opacao.write('notepad')
    escolhas_opacao.sleep(3)
    escolhas_opacao.press('enter')
    escolhas_opacao.sleep(5v          )
    escolhas_opacao.write('Escolhi o notepad')
    
