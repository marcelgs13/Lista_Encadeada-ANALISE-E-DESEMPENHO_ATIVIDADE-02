class No:
    def __init__(self, numero):
        # Método construtor que inicializa um nó com um número e um ponteiro para o próximo nó
        self.numero = numero  # Armazena o número do nó
        self.ponteiro = None  # Inicializa o ponteiro como None

    def set_ponteiro(self, ponteiro):
        # Método para definir o ponteiro para o próximo nó
        self.ponteiro = ponteiro

    def get_ponteiro(self):
        # Método para obter o ponteiro para o próximo nó
        return self.ponteiro

    def get_numero(self):
        # Método para obter o número armazenado no nó
        return self.numero