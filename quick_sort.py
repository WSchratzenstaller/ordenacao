# no metodo quick sort, um valor 'pivô' é escolhido como valor inicial para a ordenação.
# geralmente é escolhido o primeiro ou ultimo valor. A partir dele, os elementos são
# comparados entre si e irão trocar de lugar até 'alcançarem' o pivô, onde serão organizados 
# acima (maior) ou abaixo (menor) do que ele. Após a primeira execução, vão existir duas 
# partições - os valores menores e os valores maiores do que o pivô (que estará na sua posição correta).
# Recursivamente, serão escolhidos novos pivôs em ambos os lados até que todos os valores estejam ordenados.

# definição da partição
def partition(array, i, j):
    pivot = array[i]
    low = i + 1
    high = j

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[i], array[high] = array[high], array[i]

    return high

#comparação dos valores
def quick_sort(array, i, j):
    quick_sort.times += 1
    if i >= j:
        return

    p = partition(array, i, j)
    quick_sort(array, i, p-1)
    quick_sort(array, p+1, j)

#array de exemplo
array = [10, 52, 1, 70, 3, 33, 219, -70, 0, 40, 50, 1000, 9, 1001, 230]
quick_sort.times = 0

quick_sort(array, 0, len(array) - 1)
print('Array ordenado - ', array)
print('Número de recursões - ', quick_sort.times)