import time

class Relogio:

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.limparTela()

    alturaDaFonte = 5
    espacamento = 2

    fonteNumerica = [
        [
            "█████",
            "█   █",
            "█   █",
            "█   █",
            "█████"
        ],
        [
            "  █  ",
            " ██  ",
            "  █  ",
            "  █  ",
            "█████"
        ],
        [
            "█████",
            "    █",
            "█████",
            "█    ",
            "█████"
        ],
        [
            "█████",
            "    █",
            " ████",
            "    █",
            "█████"
        ],
        [
            "█   █",
            "█   █",
            "█████",
            "    █",
            "    █"
        ],
        [
            "█████",
            "█    ",
            "█████",
            "    █",
            "█████"
        ],
        [
            "█████",
            "█    ",
            "█████",
            "█   █",
            "█████"
        ],
        [
            "█████",
            "    █",
            "    █",
            "    █",
            "    █"
        ],
        [
            "█████",
            "█   █",
            "█████",
            "█   █",
            "█████"
        ],
        [
            "█████",
            "█   █",
            "█████",
            "    █",
            "█████"
        ]
    ]
    fonteSimbolos = {
        ":": [
            " ",
            "█",
            " ",
            "█",
            " "
        ]
    }

    def limparTela(self):
        print("\033[2J")

    def posicionarCursorVerticalmente(self, y):
        print("\033[{};0H".format(y))

    def esconderCursor(self):
        print("\033[?25l")

    def resetarTerminal(self):
        # Volta a mostrar o cursor escondido
        print("\033[?25h")

    def imprimir(self, string):
        framebuffer = [''] * self.alturaDaFonte
        for char in string:
            charSimbolo = self.fonteSimbolos.get(char)
            if(charSimbolo):
                for linhaIndex in range(len(charSimbolo)):
                    framebuffer[linhaIndex] += charSimbolo[linhaIndex] + ' ' * self.espacamento
                continue

            try:
                charNumero = int(char)
                for linhaIndex in range(len(self.fonteNumerica[charNumero])):
                    framebuffer[linhaIndex] += self.fonteNumerica[charNumero][linhaIndex] + ' ' * self.espacamento
            except TypeError:
                pass

        self.posicionarCursorVerticalmente(self.posy)
        for linha in framebuffer:
            print(' ' * self.posx + linha)
        self.esconderCursor()

# Cria relógio na posição [X,Y] (canto superior esquerdo)
relogio = Relogio(46, 15)
while(True):
    try:
        agora = time.localtime()
        relogio.imprimir("{:02d}:{:02d}:{:02d}".format(agora.tm_hour, agora.tm_min, agora.tm_sec))
        time.sleep(1)

    # Captura o Ctrl+C, ajusta o terminal antes de fechar
    except KeyboardInterrupt:
        relogio.resetarTerminal()
        exit()
