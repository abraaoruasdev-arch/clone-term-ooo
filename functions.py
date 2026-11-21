Verde = "\033[32m"
Amarelo = "\033[33m"
Reset = "\033[0m"


def acertouLetraVerde(letra):
    return f"{Verde}{letra}{Reset}"


def acertouLetraAmarelo(letra):
    return f"{Amarelo}{letra}{Reset}"


def banner():
    art = """
#################################################
#                                               #
#                   JOGO TERM                   #
#                                               #
#         Descubra a palavra secreta!           #
#                                               #
#                by Abbazzz                     #
#################################################
"""
    print(art)
    print("""
    #     SELECIONE A DIFICULDADE     #

    DIGITE DE 1 A 5 PARA DEFINIR QUANTAS PALAVRAS DEVE DESCOBRIR: """)
