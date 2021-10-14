def gnomeSort(valores, n):

    indice = 0

    while indice < n:

        if indice == 0:
            indice = indice + 1

        if valores[indice] >= valores[indice - 1]:
            indice = indice + 1

        else:
            aux = valores[indice]
            valores[indice] = valores[indice-1]
            valores[indice -1] = aux
            indice = indice - 1
 
    return valores

valores = [ 100,30,50,-10,0,1,5,3,900,2,4,56]
n = len(valores)

valores = gnomeSort(valores, n)
print (valores)