def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        matriz.append(linha)
    return matriz

def diagonal(tamanho):
    matriz = criar_matriz(tamanho, tamanho)
    for i in range(tamanho):
        matriz[i][i] = 'x'
    return matriz

def diagonalaocontrario(tamanho):
    matriz = criar_matriz(tamanho, tamanho)
    for i in range(tamanho):
        matriz[i][-1 -i] = 'x'
    return matriz

def diagonalaocontrario(tamanho):
    matriz = criar_matriz(tamanho, tamanho)
    coluna_max = tamanho - 1
    for i in range(tamanho):
        matriz[i][i] = 'x'
        matriz[i][coluna_max - i] = 'x'
    return matriz


from pprint import pprint
pprint(diagonal(7))
pprint(diagonalaocontrario(7))
pprint(diagonalaocontrario(7))