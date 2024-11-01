import pyautogui
import time
import keyboard  # Certifique-se de ter a biblioteca keyboard instalada com pip install keyboard

# Variável global para controlar a execução do script
executando = True

def parar_script():
    global executando
    executando = False
    print("Script interrompido pelo usuário.")

def iniciar_automacao():
    print("Aguardando 5 segundos antes de iniciar a automação...")
    time.sleep(5)  # Aguardar 10 segundos
    clicar_com_intervalo(intervalo_de_tempo, ultimo_intervalo_de_tempo, numero_de_repeticoes)

# Função para automatizar os cliques
def clicar_com_intervalo(intervalo, ultimo_intervalo, repeticoes):
    posicoes = [
        # abrir banco e aba
        (752, 108),
        # 7 cliques em cada pote + erva (a erva precisa estar no primeiro slote do banco) e fechar guia
        (629, 153), (571, 143), (686, 153), (747, 148), (1067, 52), 
        # selecionar pote e erva
        (1707, 815), (1754, 820), 
        # menu
        (318, 933),
        # abrir banco e aba
        (933, 338), (752, 108),
        # guardar objetos mochila vial
        (1708, 687), (1653, 815),
        # guardar objetos mochila potions combat
        (1755, 818), (1642, 888)
    ]
    
    for i in range(repeticoes):
        if not executando:
            break

        for index, posicao in enumerate(posicoes):
            if not executando:
                break

            pyautogui.moveTo(posicao[0], posicao[1])
            if posicao == (629, 153) or posicao == (571, 143) or posicao == (686, 153) or posicao == (747, 148):
                for _ in range(7):
                    pyautogui.click()
                    time.sleep(0.01)  # Pequeno intervalo entre os cliques múltiplos
            elif posicao == (1708, 687) or posicao == (1755, 818):
                pyautogui.click(button='right')
            else:
                pyautogui.click()
            
            if posicao == (318, 933):
                time.sleep(ultimo_intervalo)
            else:
                time.sleep(intervalo)
        
        print(f"Repetição {i+1} de {repeticoes} concluída.")

    print("Automação concluída.")

# Defina o intervalo de tempo em segundos entre cada clique
intervalo_de_tempo = 0.8  # 1 segundo para todos os cliques, exceto entre (1705, 683) e (1650, 677)
ultimo_intervalo_de_tempo = 12  # 10 segundos entre (1705, 683) e (1650, 677)

# Defina o número de repetições que a automação deve executar
numero_de_repeticoes = 71  # Por exemplo, repetir o processo 700 vezes

# Vincular a combinação de teclas Ctrl+C para parar o script
keyboard.add_hotkey('ctrl+c', parar_script)

# Iniciar a automação com atraso
print("Iniciando automação em 10 segundos. Pressione Ctrl+C para encerrar o script.")
iniciar_automacao()
