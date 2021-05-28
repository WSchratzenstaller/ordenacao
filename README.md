## Ordenação

### bubble_sort --> Algoritmo de ordenação bolha
   O algoritmo de ordenação bolha (bubble sort) compara pares adjacentes de valores e "flutua" o maior valor (ou menor se for descrescente) para a posição correta (última). 
   O laço interno garante que todos os valores serão comparados e o maior valor da vez será selecionado. Enquanto o laço externo garante que o laço interno se repetirá e selecionará o valor (primeiro maior, segundo maior, terceiro maior, etc...) conforme quantidade de vezes necessária. 
   Obs: Após ser colocado na posição correta, o valor não precisa mais ser comparado. Mas mesmo que as comparações sigam de forma redundante nas próximas "passadas" pelo laço interno, o algoritmo conseguirá ordenar o vetor da mesma forma, embora execute passos desnecessários.

### insertion_sort --> Algoritmo de ordenação por inserção
   O algoritmo de ordenação por inserção (insertion sort) compara determinado valor (a partir da segunda posição) com todos os valores anteriores e troca se algum valor anterior for maior que o valor da posição comparada.
   O laço interno garante que todos os valores anteriores a posição definida (2 - n) serão comparados. Enquanto o laço externo garante que o laço interno se repetirá a quantidade de vezes necessárias para que todos os valores tomem suas respectivas posições.

### selection_sort --> Algoritmo de ordenação por seleção
   O algoritmo de ordenação por seleção (selection sort) percorre o vetor em busca do menor valor. Em seguida transfere-o para a posição esperada.
   O laço interno busca o menor valor, o laço externo posiciona-o conforme esperado e garante qu eo laço externo se repita a quantidade de vezes necessárias para buscar o próximo menor valor até que todos estejam ordenados.  