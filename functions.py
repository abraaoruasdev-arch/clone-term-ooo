import random

# Funcoes para acerto das letras (VERDE ACERTOU A POSICAO E LETRA   -    AMARELO  ACERTOU A LETRA)\

#                           Cores 
Verde = "\033[32m"
Amarelo = "\033[33m"
Reset = "\033[0m"
def acertouLetraVerde (letra):
        print(f"{Verde}{letra}{Reset}")
def acertouLetraAmarelo (letra):
        print(f"{Amarelo}{letra}{Reset}")       



# Arte para o terminal - INTERFACE
def banner ():
    ART="""
###############################################################
#                                                             #
#        ██╗ ██████╗  ██████╗  ██████╗                        #
#        ██║██╔═══██╗██╔════╝ ██╔═══██╗                       #
#        ██║██║   ██║██║  ███╗██║   ██║                       #
#   ██   ██║██║   ██║██║   ██║██║   ██║                       #
#   ╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝                       #
#    ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝                        #
#                                                             #
#   _____ _____ ____  __  __  ____                            #
#  |_   _| ____|  _ \|  \/  |/ __ \                           #
#    | | |  _| | |_) | |\/| | |  | |                          #
#    | | | |___|  _ <| |  | | |__| |                          #
#    |_| |_____|_| \_\_|  |_|\____/                           #
#                                                             #
#         Descubra a palavra secreta!                         #
#                                              \033[38;5;141mby Abbazzz\033[0m     #
###############################################################
"""
    print(ART)



def escolherPalavraSecreta ():
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo]
