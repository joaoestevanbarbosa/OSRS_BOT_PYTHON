import pyautogui
import time
import keyboard  # Certifique-se de ter a biblioteca keyboard instalada com pip install keyboard
from datetime import datetime, timedelta

# Variável global para controlar a execução do script
executando = True

def parar_script():
    global executando
    executando = False
    print("Script interrompido pelo usuário.")

def iniciar_automacao():
    global executando
    executando = True  # Reinicia a variável executando
    print("Aguardando 10 segundos antes de iniciar a automação...")
    time.sleep(1)  # Aguardar 3 segundos
    clicar_por_tempo(intervalo_de_tempo, ultimo_intervalo_de_tempo, intervalo_ervas, duracao_total_em_horas)

# Função para calcular a duração da execução a partir do tempo de início
def clicar_por_tempo(intervalo, ultimo_intervalo, intervalo_ervas, duracao_em_horas):
    posicoes = [
        # clicar barraca
        (941, 358), (1159, 361), (941, 823), (452, 601),
        (941, 358), (1159, 361), (941, 823), (452, 601),
        (941, 358), (1159, 361), (941, 823), (452, 601),
        (941, 358), (1159, 361), (941, 823), (452, 601),
        (941, 358), (1159, 361), (941, 823), (452, 601),
        (941, 358), (1159, 361), (941, 823), (452, 601),
        (941, 358), (1159, 361), (941, 823), (452, 601),

        # mochila
        (1647, 682), (1648, 730), #ok
        (1700, 683), (1698, 730), #ok
        (1756, 680), (1757, 731), #ok
        (1802, 681), (1809, 730), #ok
        (1809, 728), (1809, 775), #ok
        (1757, 730), (1757, 775), #ok
        (1698, 723), (1699, 775), #ok
        (1648, 728), (1646, 775), #ok
        (1646, 773), (1646, 830), #ok
        (1699, 777), (1699, 830), #ok
        (1753, 773), (1753, 830), #ok
        (1804, 772), (1804, 830), #ok
        (1803, 819), (1803, 870), #ok
        (1755, 821), (1755, 870), #ok
        (1703, 818), (1703, 870), #ok
        (1647, 821), (1647, 870), #ok
        (1646, 860), (1646, 915), #ok
        (1703, 861), (1703, 915), #ok
        (1752, 865), (1752, 915), #ok
        (1808, 860), (1808, 915), #ok
        (1806, 910), (1806, 955),
        (1751, 913), (1751, 955), 
        (1699, 908), (1699, 955),
        (1653, 908), (1653, 955),
        (1651, 951), (1651, 970),
        (1704, 946), (1704, 970),
        (1755, 949), (1755, 970),
        (1806, 949), (1806, 970)
    ]

    posicoes_ervas = set([
        (1647, 682), (1700, 683), (1756, 680), (1802, 681), (1809, 728), (1757, 730),
        (1698, 723), (1648, 728), (1646, 773), (1699, 777), (1753, 773), (1804, 772),
        (1803, 819), (1755, 821), (1703, 818), (1647, 821), (1646, 860), (1703, 861),
        (1752, 865), (1808, 860), (1806, 910), (1751, 913), (1699, 908), (1653, 908),
        (1651, 951), (1704, 946), (1755, 949), (1806, 949)
    ])

    # Calcula o tempo de término com base na duração em horas
    duracao_total = duracao_em_horas * 60 * 60  # Converter horas em segundos
    tempo_de_termino = datetime.now() + timedelta(seconds=duracao_total)

    while datetime.now() < tempo_de_termino:
        if not executando:
            break

        for index, posicao in enumerate(posicoes):
            if not executando or datetime.now() >= tempo_de_termino:
                break
            
            pyautogui.moveTo(posicao[0], posicao[1])
         
            if posicao in posicoes_ervas:
                pyautogui.click(button='right')
                time.sleep(intervalo_ervas)
            else:
                pyautogui.click()
                time.sleep(intervalo)
            
            if posicao == (941, 358) or posicao == (1159, 361) or posicao == (941, 823) or posicao == (452, 601):
                time.sleep(ultimo_intervalo)

        print("Ciclo de cliques completado.")
    
    print("Automação concluída com base no tempo definido.")

# Defina o intervalo de tempo em segundos entre cada clique
intervalo_de_tempo = 0.15  # Intervalo padrão para cliques
intervalo_ervas = 0.3  # Intervalo menor para cliques ao limpar ervas
ultimo_intervalo_de_tempo = 3.0  # Intervalo maior entre etapas específicas

# Defina a duração total em horas
duracao_total_em_horas = 1.1 # Por exemplo, 2 horas

# Vincular a combinação de teclas Ctrl+C para parar o script
keyboard.add_hotkey('ctrl+c', parar_script)

# Iniciar a automação com atraso
print("Iniciando automação. Pressione Ctrl+C para encerrar o script.")
iniciar_automacao()
