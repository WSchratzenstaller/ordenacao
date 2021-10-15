def comb_sort(valores):
    n = len(valores)
    gap = n
    swap = True
    while gap > 1 or swap:
        gap = max(1, int(gap / 1.3))
        swap = False
        for i in range(0, n - gap):
            j = i + gap
            if valores[i] > valores[j]:
                valores[i], valores[j] = valores[j], valores[i]
                swap = True
    return valores

valores = [5, 4, 3, 2, 1, 6, 0]
print(comb_sort(valores))