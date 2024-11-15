const fs = require('fs');
const path = require('path');
const LinkedList = require('./LinkedList');

function readInput(filePath) {
    try {
        const data = fs.readFileSync(filePath, 'utf8').split('\n');
        return data;
    } catch (error) {
        console.error(`Erro ao ler o arquivo ${filePath}:`, error.message);
        process.exit(1);
    }
}

function writeOutput(filePath, content) {
    try {
        const fullPath = path.resolve(filePath);
        fs.writeFileSync(fullPath, content, 'utf8');
        console.log(`Arquivo salvo em: ${fullPath}`);
    } catch (error) {
        console.error(`Erro ao escrever no arquivo ${filePath}:`, error.message);
    }
}

function appendPerformanceLog(filePath, content) {
    try {
        const fullPath = path.resolve(filePath);
        fs.appendFileSync(fullPath, content, 'utf8');
        console.log(`Desempenho registrado em: ${fullPath}`);
    } catch (error) {
        console.error(`Erro ao registrar desempenho em ${filePath}:`, error.message);
    }
}

function process(filePath) {
    const data = readInput(filePath);

    if (data.length < 2) {
        console.error("Erro: O arquivo de entrada deve conter ao menos duas linhas.");
        process.exit(1);
    }

    const numbers = data[0].split(' ').map(Number);
    const totalCommands = parseInt(data[1], 10);

    if (isNaN(totalCommands)) {
        console.error("Erro: A segunda linha do arquivo de entrada deve conter um número válido.");
        process.exit(1);
    }

    const commands = data.slice(2, 2 + totalCommands);
    const list = new LinkedList();

    numbers.forEach((num) => list.add(num, 999));

    commands.forEach((cmd) => {
        const parts = cmd.split(' ');
        try {
            if (parts[0] === 'A') {
                const value = parseInt(parts[1], 10);
                const position = parts.length > 2 ? parseInt(parts[2], 10) : 0;
                list.add(value, position);
            } else if (parts[0] === 'R') {
                const value = parseInt(parts[1], 10);
                list.remove(value);
            } else if (parts[0] === 'P') {
                list.print();
            } else {
                console.error(`Comando inválido: ${cmd}`);
            }
        } catch (error) {
            console.error(`Erro ao processar comando ${cmd}:`, error.message);
        }
    });

    return list;
}

function main() {
    const inputFile = '../arq-novo.txt'; // Nome do arquivo de entrada
    const outputFile = './output.txt'; // Arquivo de saída da lista final
    const performanceFile = './performance.txt'; // Arquivo de saída do tempo de execução

    const startTime = Date.now();
    const list = process(inputFile);
    const executionTime = (Date.now() - startTime) / 1000;

    // Gerando saída final
    const result = [];
    let current = list.head;

    while (current) {
        result.push(current.value);
        current = current.next;
    }

    writeOutput(outputFile, result.join(' '));


    // Registrando desempenho
    appendPerformanceLog(performanceFile, `Execution Time: ${executionTime.toFixed(3)} s\n`);

    console.log(`Lista final salva em ${outputFile}`);
    console.log(`Tempo de execução registrado em ${performanceFile}`);
}

main();
