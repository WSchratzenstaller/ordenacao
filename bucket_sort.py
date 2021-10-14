def bucket_sort(valores):
    # Encontra o valor máximo na lista e use o comprimento da lista para determinar qual valor da lista vai para qual bucket 
    maior_elemento = max(valores)
    tamanho = maior_elemento/len(valores)

    # Cria n baldes vazios onde n é igual ao tamanho da lista 
    lista_buckets= []
    for x in range(len(valores)):
        lista_buckets.append([]) 

    # Coloca os elementos da lista em diferentes grupos com base no tamanho
    for i in range(len(valores)):
        auxiliar = int(valores[i] / tamanho)
        if auxiliar != len (valores):
            lista_buckets[auxiliar].append(valores[i])
        else:
            lista_buckets[len(valores) - 1].append(valores[i])

    # Ordena os elementos dentro dos buckets
    for z in range(len(valores)):
        insertion_sort(lista_buckets[z])
            
    # Concatena os buckets ordenados em uma unica lista
    lista_ordenada = []
    for x in range(len (valores)):
        lista_ordenada = lista_ordenada + lista_buckets[x]
    return lista_ordenada

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

def main():
    valores = [1.20, 0.22, 0.43, 0.36, 0.39, 0.27, 100, 2320, 500, 1000234]
    print('LISTA ORIGINAL:')
    print(valores)
    lista_ordenada = bucket_sort(valores)
    print('LISTA ORDENADA:')
    print(lista_ordenada)

main()