import pyautogui
import time
import keyboard
from datetime import datetime, timedelta

# Variável global para controlar a execução do script
executando = True

def parar_script():
    """Para a execução do script ao pressionar Ctrl+C."""
    global executando
    executando = False
    print("Script interrompido pelo usuário.")

def iniciar_automacao():
    """Inicia a automação após um atraso de 5 segundos."""
    global executando
    executando = True  # Reinicia a variável executando
    print("Aguardando 5 segundos antes de iniciar a automação...")
    time.sleep(5)  # Aguardar 5 segundos
    clicar_por_tempo(intervalo_de_tempo, ultimo_intervalo, duracao_total_em_horas)

def clicar_por_tempo(intervalo, ultimo_intervalo, duracao_em_horas):
    """Realiza cliques em posições predefinidas durante um tempo especificado."""

    posicoes = [
        # abrir banco e aba
        #(944, 331), 
        #(390, 956), (350, 879),

        #manter menu aberto
        (752, 108),

        (627,149), # barra
        (571, 143), # coal

        #andando ate a bigorna
        #(1784, 316),
        (1100,999),

        #menu de platebody
        (712, 501),

        #andar até o banco e abrir banco
        #(22, 744), 
        (850,210),
        

        # #guardar mochila
        (1007, 783),
        (1007, 783) ##guardando 2x pq tá com bug
        # fechar guia
        #(1067, 52)

    ]

    duracao_total = duracao_em_horas * 3600  # Converter horas em segundos
    tempo_de_termino = datetime.now() + timedelta(seconds=duracao_total)

    while datetime.now() < tempo_de_termino:
        if not executando:
            print("Execução interrompida.")
            break

        for index, posicao in enumerate(posicoes):
            if not executando or datetime.now() >= tempo_de_termino:
                break

            try:
                pyautogui.moveTo(posicao[0], posicao[1])
                pyautogui.click()

                if posicao == (1100, 999):  #andar ate a bigorna
                    time.sleep(8)

                elif posicao == (627, 149):  # barra
                    for _ in range(26): 
                        pyautogui.click()
                        time.sleep(0.1)

                elif posicao == (571, 143):  # martelo
                    for _ in range(0): 
                        pyautogui.click()
                        time.sleep(0.1)

                elif posicao == (712, 501):  # menu platebody
                    time.sleep(15)

                elif posicao == (850, 210):  # andar até o banco
                    time.sleep(8)

                time.sleep(intervalo)

            except Exception as e:
                print(f"Erro ao clicar na posição {posicao}: {e}")
                parar_script()

        print(f"Ciclo de cliques {index + 1}/{len(posicoes)} completado.")

    print("Automação concluída ou tempo definido alcançado.")

# Configurações da automação
intervalo_de_tempo = 0.90  # Intervalo entre os cliques em segundos
ultimo_intervalo = 3  # Intervalo especial entre alguns cliques
duracao_total_em_horas = 5.8  # Duração total da automação em horas

# Vincular a combinação de teclas Ctrl+C para parar o script
keyboard.add_hotkey('ctrl+c', parar_script)

# Iniciar a automação
print("Iniciando automação. Pressione Ctrl+C para encerrar o script.")
iniciar_automacao()
