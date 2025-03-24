import sys, numpy, igraph

# lê um arquivo e coloca seus dados em uma matriz
def lerMatriz(fileName):
    path = './grafos_datasets/' + fileName
    m = []
    with open(path, 'r') as f:
        for line in f:
            m.append(list(map(int, line.split())))
    return numpy.array(m)

# salva o nome da instância, quantidade de linhas e colunas em resultado.txt
def salvarDados(instanceName, qtyLine, qtyColumn):
    f = open('resultado.txt', 'w')
    f.write('{0} {1} {2}'.format(instanceName, qtyLine, qtyColumn))
    f.close()

def main(fileName):
    matriz = lerMatriz(fileName)
    line, col = matriz.shape
    salvarDados(fileName, line, col)

if __name__ == '__main__':
    main(str(sys.argv[1]))