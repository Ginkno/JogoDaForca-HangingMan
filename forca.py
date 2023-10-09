# JOGO DA FORCA
# inputs: lista de palavras em portugues, input do usuario
# display: mostra o tamanho da palavra escolhida e pede para o usuario escolher letra
# processamento: escolhida a letra, se certa, mostra. Se errada, perde uma vida.
# saida: match palavra inteira (ganha)/ not match, perde todas as vidas (perde)

import os
import random
import numpy as np
import pandas as pd
from colorama import Fore, Style, Back


def jogar():

    df = pd.read_csv(r'C:\Users\Contratos\Downloads\palavras.txt')

    # aplicar formula para selecionar apenas palavras que tenham acima de 3 ou mais letras
    plv = df['a'].apply(lambda x: x if len(x) > 2 else np.nan)

    # aplica formula para pegar uma dessas palavras de forma aleatoria
    sample = plv.sample(n=1)
    plv_sec = sample.values
    # print da plv_sec para controle na elaboração
    # print(plv_sec)



    ## PARÂMETROS DE CONTROLE DO JOGO DA FORCA
    # VIDAS : seram mantidas quando palpite certo e tiradas quando errado
    # miss_c : controle do char "-" para conferir se ainda existem na palavra escondida
    # palavra_teste : palavra recebida do dicionário de palavras, transformada em lista de caracteres.
    # será a palavra alvo a ser encontrada pelo usuário
    # palavra_hid : string criada a partir do mesmo tamanho da palavra teste, com caracteres "-" no lugar
    # das letras da palavra alvo

    vidas = 7
    miss_c = "-"
    palavra_teste = list(" ".join(map(str, plv_sec)))
    palavra_hid = list("-" * len(palavra_teste))
    confere_chute = []
    YELLOW = "\x1b[1;33;40m"

    ### PROCESSAMENTO

    #função adivinha, processa as entradas do usuário e retorna de acordo
    def adivinha(vidas, palavra_hid, palavra_teste, confere_chute):

        ## OUTPUT NEGATIVO - Resultado quando o usuário perde todas as vidas
        if vidas < 1:
            plv = ''.join(palavra_teste)
            print("\n")
            print("Vidas: 0. Você Perdeu. Fim do Jogo")
            print("A palavra secreta era: ", plv)
            novo_jogo = input("Deseja jogar novamente (y|n)? ")
            if novo_jogo == "y":
                jogar()
            else:
                exit()

        ## OUTPUT POSITIVO - Resultado quando o usuario acerta a palavra inteira
        if palavra_hid == palavra_teste:
            res = ''.join(palavra_hid)
            print("\n")
            print("Você adivinhou. A palavra certa é", res)
            novo_jogo = input("Deseja jogar novamente (y|n)? ")
            if novo_jogo == "y":
                jogar()
            else:
                exit()

        # Prints para checar funcionamento do código durante elaboração
        print("Vidas: ", vidas)
        # print(palavra_teste)
        print(palavra_hid)

        ## INPUT DO USUÁRIO E TRATAMENTO
        # checar se usuário coloca um única letra como entrada. Trata letra maiusculas para minusculas
        while True:
            print(Fore.LIGHTYELLOW_EX + "Digite uma nova letra: " + Style.RESET_ALL, end='')
            letra_chute = input()
            print("\n")

            if len(letra_chute) == 1 and letra_chute.isalpha() and letra_chute not in confere_chute:
                confere_chute.append(letra_chute)
                letra_chute = letra_chute.lower()
                break
            else:
                print("Digite apenas uma única letra, sem repetição")
                continue

        # cria uma lista para os indices das letras que correspondem as letras respondidas pelo usuario
        lista_chute = [i for i, n in enumerate(palavra_teste) if n == letra_chute]

        # while loop que checa se existem "-" na palavra escondida. Se ainda houver, continua...
        while miss_c in palavra_hid:
            # se a letra escolhida nao corresponder a palavra alvo, a lista de chute será vazia
            # e o usuário perde vidas. Ao final, chama a função novamente
            if len(lista_chute) == 0:
                vidas = vidas-1
                print(Fore.LIGHTRED_EX + "Você perdeu uma vida" + Style.RESET_ALL)
                adivinha(vidas, palavra_hid, palavra_teste, confere_chute)
            else:
            # se a letra corresponder a palavra, usuario recebe feedback e a palavra com "-"
            # recebe as letras correspondentes no índice correspondente
                print(lista_chute) # print dos índices encontrados
                print(Fore.LIGHTGREEN_EX + "Você acertou." + Style.RESET_ALL)
                for chute in lista_chute:
                    palavra_hid[chute] = letra_chute
                adivinha(vidas, palavra_hid, palavra_teste, confere_chute)

    adivinha(vidas, palavra_hid, palavra_teste, confere_chute)
jogar()


