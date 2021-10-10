def bucket_sort(valores):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    Maior_Elemento = max(valores)
    tamanho = Maior_Elemento/len(valores)

    # Create n empty buckets where n is equal to the length of the input list
    Lista_Buckets= []
    for x in range(len(valores)):
        Lista_Buckets.append([]) 

    # Put list elements into different buckets based on the tamanho
    for i in range(len(valores)):
        auxiliar = int(valores[i] / tamanho)
        if auxiliar != len (valores):
            Lista_Buckets[auxiliar].append(valores[i])
        else:
            Lista_Buckets[len(valores) - 1].append(valores[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(valores)):
        insertion_sort(Lista_Buckets[z])
            
    # Concatenate buckets with sorted elements into a single list
    Lista_Ordenada = []
    for x in range(len (valores)):
        Lista_Ordenada = Lista_Ordenada + Lista_Buckets[x]
    return Lista_Ordenada

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
    print('ORIGINAL LIST:')
    print(valores)
    sorted_list = bucket_sort(valores)
    print('SORTED LIST:')
    print(sorted_list)

main()