def heap(valores, n, i):
    raiz = i  #inicia a raíz
    esquerda = 2 * i + 1     
    direita = 2 * i + 2    
 
    # ve se o galho direito da raíz existe e se é raiz que a raíz
    if esquerda < n and valores[raiz] < valores[esquerda]:
        raiz = esquerda
 
    # ve se o galho direito da raíz existe e se é raiz que a raíz
    if direita < n and valores[raiz] < valores[direita]:
        raiz = direita
 
    # muda a raíz se necessário
    if raiz != i:
        auxiliar = valores[i]
        valores[i] = valores [raiz]
        valores[raiz] = auxiliar
        heap(valores, n, raiz)
 
 
 
def heapSort(valores):
    n = len(valores)
 
    # formação da maxheap
    for i in range(n//2 - 1, -1, -1):
        heap(valores, n, i)
 
    # puxar elementos respectivamente
    for i in range(n-1, 0, -1):
        auxiliar = valores[i]
        valores[i] = valores[0]
        valores[0] = auxiliar
        heap(valores, i, 0)
    
    return valores
 
valores = [10,65,23,123,2,21,321,32,43,53,3,44]
valores_ordenados = heapSort(valores)
n = len(valores)
print("Grupo ordenado: ", valores_ordenados)

