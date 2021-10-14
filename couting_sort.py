
def countingSort(valores):
    tamanho = len(valores)
    auxiliar = [0] * tamanho

    x = [0] * 10

    for i in range(0, tamanho):
        x[valores[i]] += 1

    for i in range(1, 10):
        x[i] += x[i - 1]

    i = tamanho - 1
    while i >= 0:
        auxiliar[x[valores[i]] - 1] = valores[i]
        x[valores[i]] -= 1
        i -= 1

    for i in range(0, tamanho):
        valores[i] = auxiliar[i]

    return valores

valores = [1, 9, 1, 6, 7, 3, 7]
valoresOrdenados = countingSort(valores)
print(valores)
