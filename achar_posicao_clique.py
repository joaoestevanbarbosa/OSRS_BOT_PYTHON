import pyautogui


# https://daftsex.org/familystrokes-katie-kush-sophia-locke-summer-stevens-our-stepmom-is-fucking-someone-lets-listen-08-22-2024/


def capturar_posicoes():
    posicoes = []
    print("Posicione o cursor e pressione 'Enter' para capturar a posição. Pressione 'q' para sair.")
    
    while True:
        input("Pressione 'Enter' para capturar a posição ou 'q' para sair: ")
        if input().lower() == 'q':
            break
        posicao = pyautogui.position()
        posicoes.append(posicao)
        print(f"Posição capturada: {posicao}")
    
    return posicoes

# Captura as posições
posicoes = capturar_posicoes()

# Exibe todas as posições capturadas
print("Posições capturadas:")
for posicao in posicoes:
    print(posicao)