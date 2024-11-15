import time
from ListaEncadeada import ListaEncadeada


class App:
    @staticmethod
    def ler_entrada(nome):
        # Método para ler os dados do arquivo
        arq = open(nome, 'r')
        dat = arq.readlines()
        arq.close()
        return dat

    @staticmethod
    def processar(caminho):
        # Método para processar os comandos do arquivo
        dados_arquivo = App.ler_entrada(caminho)
        # Primeira linha contém os números iniciais
        numeros = dados_arquivo[0].split()
        # Segunda linha contém o número total de comandos
        total_entradas = int(dados_arquivo[1])
        comandos = []
        for i in range(2, total_entradas + 2):
            # Restante das linhas contém os comandos
            comandos.append(dados_arquivo[i].split())
        lista = ListaEncadeada()  # Cria uma instância da lista encadeada
        for dat in numeros:
            # Adiciona os números iniciais na lista
            lista.adicionar(int(dat), 999)
        for cmd in comandos:
            # Itera sobre os comandos e executa as ações correspondentes
            if cmd[0] == 'A':
                if len(cmd) == 2:
                    # Adiciona o número na posição indicada
                    lista.adicionar(int(cmd[1]), 0)
                else:
                    # Adiciona o número na posição indicada
                    lista.adicionar(int(cmd[1]), int(cmd[2]))
            elif cmd[0] == 'R':
                lista.remover(int(cmd[1]))  # Remove o número indicado
            elif cmd[0] == 'P':
                lista.imprimir()  # Imprime a lista


if __name__ == "__main__":
    # Função principal que executa o processamento do arquivo
    inicial = time.time()
    App.processar("arq-novo.txt")
    tempo_total = time.time() - inicial  # Calcula o tempo total em segundos

    # Imprime e salva o tempo total em segundos no arquivo de medição
    print(f"Tempo total: {tempo_total:.6f} segundos")
    with open("Medir Py.txt", 'a') as arq:
        arq.write(f"Tempo total: {tempo_total:.6f} segundos\n")
