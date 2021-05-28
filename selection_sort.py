# Algoritmo de ordenação SelectionSort/Seleção
def selection_sort(valores):
    n = len(valores)
    for i in range(0, n-1, +1): #i = indice//in valores => i = item 
        menor = i
        for j in range(i+1, n, +1):
            if (valores[j] < valores[menor]):
                menor = j
        auxiliar = valores[i]
        valores[i] = valores[menor]
        valores[menor] = auxiliar
    return valores

# Chamada para teste
valores = [5, 4, 3, 2, 1, 6, 0]
print(selection_sort(valores))