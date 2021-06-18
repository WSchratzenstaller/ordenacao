#Algoritmo de ordenação Merge/Mescla
def merge(valores_esquerdos, valores_direitos):
    valores_ordenados = [ ]
    while valores_esquerdos or valores_direitos:
        if len(valores_esquerdos) and len(valores_direitos):
            if valores_esquerdos[0] < valores_direitos[0]:
                valores_ordenados.append(valores_esquerdos.pop(0))
            else:
                valores_ordenados.append(valores_direitos.pop(0))
        if not len(valores_esquerdos):
            if len(valores_direitos):
                # poderia transferir todo o lado direito e sair do laço
                valores_ordenados.append(valores_direitos.pop(0))
        if not len(valores_direitos):
            if len(valores_esquerdos):
                # poderia transferir todo o lado esquerdo e sair do laço
                valores_ordenados.append(valores_esquerdos.pop(0))
    return valores_ordenados

def merge_sort(valores):
    if len(valores) < 2:
        return valores
    meio = int(len(valores)/2)
    return merge(merge_sort(valores[:meio]), merge_sort(valores[meio:]))

# Chamada para teste
valores = [5, 4, 3, 2, 1, 6, 0]
print(merge_sort(valores))

