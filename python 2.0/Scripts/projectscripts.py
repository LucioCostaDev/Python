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
    escolhas_opacao.hotkey('win', 'r')
    escolhas_opacao.sleep(3)
    escolhas_opacao.write('excel')
    escolhas_opacao.press('enter')
    escolhas_opacao.write('Escolhi o Excel')
elif opcao == "Word":
    escolhas_opacao.hotkey('win', 'r')
    escolhas_opacao.sleep(3)
    escolhas_opacao.write('word')
    escolhas_opacao.press('enter')
    escolhas_opacao.writer('Escolhi o Word')    
elif opcao == "Notepad":
    escolhas_opacao.hotkey('win', '')
    print("Escolheu Notepad")
