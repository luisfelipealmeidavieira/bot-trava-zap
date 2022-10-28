import pyautogui
from time import sleep
 
MSG=input('Qual é a mensagem? ')
QNT=int(input('Quantas mensagens? '))
print("Por favor, coloque o cursor no campo de enviar a mensagem do telegram.")
print("O bot vai começar a colar a mensagem '",MSG,"', ",QNT," vezes, em 3 segundos")
sleep(3)
for TIMES in range(QNT):
    pyautogui.write(MSG)
    pyautogui.hotkey('enter')
