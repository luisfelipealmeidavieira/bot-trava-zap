import pyautogui
from time import sleep
 
MSG=input('Qual é a mensagem? ')
QNT=int(input('Quantas mensagens? '))
current_quantity = 0
print("Por favor, coloque o cursor no campo de enviar a mensagem do telegram.")
print("O bot vai começar a colar a mensagem '",MSG,"', ",QNT," vezes, em 3 segundos")
sleep(3)
for TIMES in range(QNT):
    current_quantity += 1
    print("CURRENT QUANTITY: ", current_quantity)
    pyautogui.write(MSG)
    pyautogui.hotkey('enter')
