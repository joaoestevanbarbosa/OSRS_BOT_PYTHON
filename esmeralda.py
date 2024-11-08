import pyautogui
import time

# Função para automatizar os cliques
def clicar_com_intervalo(intervalo, ultimo_intervalo, tempo_maximo):
    posicoes = [
        ## abrir banco e aba
        (944, 331), (390, 956), (350, 879), (752, 108),
        ## 27 cliques da esmeralda e fechar guia
        (571, 143), (1067, 52), 
        ## crafting, esperar 40 segundos após (318,933)
        (1705, 683), (1650, 677), 
        ## menu crafting 3
        (318, 933),
         ## abrir banco e aba
        (944, 331), (390, 956), (350, 879), (752, 108),
         ## guardar objetos mochila
        (1708, 687), (1653, 815),
        ## fechar guia
        (1067, 52)
    ]
    
    # Registrar o tempo inicial
    tempo_inicial = time.time()

    while True:
        # Registrar o tempo atual
        tempo_atual = time.time()
        
        # Calcular o tempo decorrido
        tempo_decorrido = tempo_atual - tempo_inicial
        
        # Verificar se o tempo máximo foi atingido
        if tempo_decorrido >= tempo_maximo:
            print("O tempo máximo foi atingido!")
            break
        
        for index, posicao in enumerate(posicoes):
            # Mover o mouse para a posição especificada e clicar
            pyautogui.moveTo(posicao[0], posicao[1])
            if posicao == (571, 143):
                # Clicar 27 vezes na posição (571, 143)
                for _ in range(27):
                    pyautogui.click()
                    time.sleep(0.1)  # Pequeno intervalo entre os cliques múltiplos
            elif posicao == (1708, 687):
                # Clique com o botão direito na posição (1705, 683)
                pyautogui.click(button='right')
            else:
                pyautogui.click()
            # Esperar o tempo especificado antes do próximo clique
            if posicao == (318, 933):
                time.sleep(ultimo_intervalo)
            else:
                time.sleep(intervalo)
        
        # Mostrar o tempo restante
        tempo_restante = tempo_maximo - tempo_decorrido
        print(f"Você tem {tempo_restante:.2f} segundos restantes.")

    print("Automação concluída.")

# Defina o intervalo de tempo em segundos entre cada clique
intervalo_de_tempo = 0.95  # 1 segundo para todos os cliques, exceto entre (1705, 683) e (1650, 677)
ultimo_intervalo_de_tempo = 34  # 50 segundos entre (1705, 683) e (1650, 677)

# Defina o tempo máximo (em segundos) que a automação deve executar
tempo_maximo = 100  # Por exemplo, 10 minutos (600 segundos) 19800

# Iniciar a automação
print("Iniciando automação.")
clicar_com_intervalo(intervalo_de_tempo, ultimo_intervalo_de_tempo, tempo_maximo)