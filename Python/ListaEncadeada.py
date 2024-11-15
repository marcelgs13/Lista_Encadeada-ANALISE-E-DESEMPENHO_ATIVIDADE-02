from No import No  # Importa a classe No para utilizar os nós na lista encadeada


class ListaEncadeada:
    def __init__(self):
        # Inicializa a lista encadeada com a cabeça (primeiro nó) como None
        self.cabeca = None

    def adicionar(self, numero, posicao):
        # Método para adicionar um novo nó com o número dado na posição especificada na lista encadeada
        novo = No(numero)  # Cria um novo nó com o número dado
        if self.cabeca is None:
            # Se a lista estiver vazia, define o novo nó como a cabeça da lista
            self.cabeca = novo
        else:
            # Se a lista não estiver vazia, percorre até a posição desejada e insere o novo nó lá
            atual = self.cabeca
            for i in range(posicao-1):
                if atual.get_ponteiro() is None:
                    break  # Se chegar ao final da lista, para
                atual = atual.get_ponteiro()  # Move para o próximo nó
            # Define o próximo do novo nó
            novo.set_ponteiro(atual.get_ponteiro())
            # Define o novo nó como próximo do nó atual
            atual.set_ponteiro(novo)

    def remover(self, numero):
        # Método para remover o nó com o número dado da lista encadeada
        if self.cabeca is None:
            return -1  # Retorna -1 se a lista estiver vazia
        if self.cabeca.get_ponteiro() is None:
            # Se houver apenas um nó na lista e for igual ao número dado, remove-o
            self.cabeca = None
            return -1
        if self.cabeca.get_numero() == numero:
            # Se o primeiro nó contiver o número dado, redefine a cabeça para o próximo nó
            self.cabeca = self.cabeca.get_ponteiro()
            return 1
        atual = self.cabeca
        while atual.get_ponteiro() is not None:
            # Percorre a lista até encontrar o nó com o número dado
            if atual.get_ponteiro().get_numero() == numero:
                atual.set_ponteiro(
                    atual.get_ponteiro().get_ponteiro())  # Remove o nó
                return 1
            atual = atual.get_ponteiro()  # Move para o próximo nó

    def imprimir(self):
        # Método para imprimir os números armazenados na lista encadeada
        lista = []  # Inicializa uma lista vazia para armazenar os números da lista encadeada
        atual = self.cabeca
        while atual is not None:
            # Percorre a lista encadeada e adiciona os números à lista
            lista.append(atual.get_numero())
            atual = atual.get_ponteiro()  # Move para o próximo nó
        print(lista)  # Imprime a lista de números