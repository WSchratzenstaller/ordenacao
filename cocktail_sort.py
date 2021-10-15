def cocktail_sort(valores):
    condicao = True
    while condicao:
        condicao = False

        #Primeiro laço leva os maiores valores até o fim da lista.
        for i in range(len(valores)-1):
            if valores[i] > valores[i+1]:
                valores[i], valores[i+1] = valores[i+1], valores[i]
                condicao = True
        
        #Se a condição for "False" significa que os valores estão ordenados.
        #Encerra os laços.
        if not condicao:
            return valores

        #Segundo laço leva os menores valores até o início da lista.
        for j in range(len(valores)-2, 0, -1):
            if valores[j] < valores[j-1]:
                valores[j], valores[j-1] = valores[j-1], valores[j]
                condicao = True

#exemplo
valores = [17, 29, 2, 3, 7, 11, 37, 19]
print(cocktail_sort(valores))


