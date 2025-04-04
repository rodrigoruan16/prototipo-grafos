import sys, numpy

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
    s = '{0} {1} {2}'.format(instanceName, qtyLine, qtyColumn)
    f = open('resultado.txt', 'w')
    f.write(s)
    f.close()
    print(s)

def main(fileName):
    matrix = lerMatriz(fileName)
    line, col = matrix.shape
    salvarDados(fileName, line, col)

if __name__ == '__main__': # verifica se o script está sendo rodado como programa central e não foi importado como módulo
    main(str(sys.argv[1]))