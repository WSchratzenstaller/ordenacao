# No metodo gnomeSort temos um numero que vai percorrendo toda a lista se ele enauxrar um numero maior que ele ele faz a troca 
# caso ele não enauxre ele anda até o final da lista, caso não tenha nenhum numero maior ele é solto no final da lista


#criação do metodo
def gnomeSort(aux, n):
    #posição da lista
    indice = 0

    while indice < n:

        if indice == 0:
            indice = indice + 1
        # se minha posição or maior ou igual ao numero anterior eu pulo uma casa
        if aux[indice] >= aux[indice - 1]:
            indice = indice + 1

        else:
            aux[indice], aux[indice-1] = aux[indice-1], aux[indice]
            indice = indice - 1
 
    return aux
#valores que vão entrar na ordenação
valores = [ 100,30,50,-10,0,1,5,3,900,2,4,56]
n = len(valores)
 #resultado
valores = gnomeSort(valores, n)
print (valores)