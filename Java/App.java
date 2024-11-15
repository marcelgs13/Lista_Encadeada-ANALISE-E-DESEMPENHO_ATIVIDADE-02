package Java;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws FileNotFoundException {
        long inicio = System.nanoTime(); // Início da execução

        // Inicializa a lista encadeada e processa o arquivo arq-novo.txt
        ListaEncadeada lista = new ListaEncadeada();
        processarArquivo("arq-novo.txt", lista, "saida_arq-novo.txt");

        long fim = System.nanoTime(); // Fim da execução
        long duracao = fim - inicio; // Duração em nanossegundos
        double duracaoSegundos = duracao / 1_000_000_000.0; // Convertendo para segundos

        System.out.printf("Tempo total de execução: %.3f segundos%n", duracaoSegundos);

        // Salva o tempo de execução no arquivo
        salvarTempoExecucao("tempo_medio_execucao.txt", duracaoSegundos);
    }

    public static void processarArquivo(String nomeArquivo, ListaEncadeada listaEncadeada, String arquivoSaida) {
        try {
            File file = new File(nomeArquivo);
            Scanner scanner = new Scanner(file);

            // Lê a primeira linha do arquivo e adiciona números à lista
            String[] numerosIniciais = scanner.nextLine().trim().split("\\s+");
            for (String numero : numerosIniciais) {
                listaEncadeada.inserirNoFinal(Integer.parseInt(numero));
            }

            // Lê os comandos para processar a lista
            int totalEntradas = Integer.parseInt(scanner.nextLine().trim());
            for (int i = 0; i < totalEntradas; i++) {
                String linha = scanner.nextLine().trim();
                String[] comando = linha.split("\\s+");

                if (comando.length < 2 && !comando[0].equals("P")) {
                    System.out.println("Comando inválido: " + linha);
                    continue;
                }

                String nomeAcao = comando[0];
                if (nomeAcao.equals("P")) {
                    listaEncadeada.imprimirLista();
                } else {
                    int numero = Integer.parseInt(comando[1]);
                    if (nomeAcao.equals("A") && comando.length == 3) {
                        int posicao = Integer.parseInt(comando[2]);
                        listaEncadeada.adicionarNaPosicao(posicao, numero);
                    } else if (nomeAcao.equals("R")) {
                        listaEncadeada.remover(numero);
                    } else {
                        System.out.println("Comando inválido: " + linha);
                    }
                }
            }

            System.out.println("Lista final após o processamento do arquivo " + nomeArquivo + ":");
            listaEncadeada.imprimirLista();

            // Salva o conteúdo da lista no arquivo de saída
            salvarListaEmArquivo(listaEncadeada, arquivoSaida);

            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado: " + nomeArquivo);
        }
    }

    public static void salvarListaEmArquivo(ListaEncadeada lista, String nomeArquivo) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(nomeArquivo))) {
            No atual = lista.cabeca;
            while (atual != null) {
                writer.write(atual.dado + " ");
                atual = atual.proximo;
            }
            writer.newLine();
            System.out.println("Lista salva em: " + nomeArquivo);
        } catch (IOException e) {
            System.out.println("Erro ao salvar a lista no arquivo: " + e.getMessage());
        }
    }

    public static void salvarTempoExecucao(String nomeArquivo, double tempoExecucao) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(nomeArquivo, true))) {  // O 'true' faz com que o tempo seja adicionado no final do arquivo
            writer.write(String.format("%.3f%n", tempoExecucao));  // Formata para 3 casas decimais
            System.out.printf("Tempo de execução salvo em '%s': %.3f segundos%n", nomeArquivo, tempoExecucao);
        } catch (IOException e) {
            System.out.println("Erro ao salvar o tempo de execução: " + e.getMessage());
        }
    }
}
