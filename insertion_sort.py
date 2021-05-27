# Algoritmo de ordenação InsertionSort/Inserção
def insertion_sort(valores):
    n = len(valores)
    for i in range(1, n, +1):
        chave = valores[i]
        j = i - 1
        while (j > -1 and valores[j] > chave):
            valores[j+1] = valores[j]
            j -= 1
        valores[j+1] = chave
    return valores

# Chamada para teste
valores = [5, 4, 3, 2, 1, 6, 0]
print(insertion_sort(valores))