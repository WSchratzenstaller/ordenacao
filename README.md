## Ordenação

### bubble_sort --> Algoritmo de ordenação bolha
   O algoritmo de ordenação bolha (bubble sort) compara pares adjacentes de valores e "flutua" o maior valor (ou menor se for descrescente) para a posição correta (última). 
   O laço interno garante que todos os valores serão comparados e o maior valor da vez será selecionado. Enquanto o laço externo garante que o laço interno se repetirá e selecionará o valor (primeiro maior, segundo maior, terceiro maior, etc...) conforme quantidade de vezes necessária. 
   Obs: Após ser colocado na posição correta, o valor não precisa mais ser comparado. Mas mesmo que as comparações sigam de forma redundante nas próximas "passadas" pelo laço interno, o algoritmo conseguirá ordenar o vetor da mesma forma, embora execute passos desnecessários.

### Cocktail Sort --> Algoritmo de ordenação coquetel
   O Cocktail sort é um método de ordenação por comparação, ele ordena o vetor ou os valores inseridos de forma semelhante ao bubble sort. O cocktail sort é composto por dois laços de repetição, começa comparando da esquerda para a direita, verificando se o valor da esquerda é maior que o da direita, levando os maiores valores para o final, se for verdadeiro, ele faz a troca, assim, sucessivamente até o final do vetor, após chegar no final do vetor, ele volta comparando se o valor da esquerda é maior que o da direita, levando os menores valores para o início, assim ate que o vetor ou conjunto de valores esteja ordenado.
   By Alelovers (padrão diferente) 

### Heapsort 
   É um método de ordenação cujo princípio de funcionamento é o mesmo utilizado para a ordenação por seleção. O heapsort utiliza uma estrutura de dados chamada heap binário para ordenar os elementos à medida que os insere na estrutura. Assim, ao final das inserções, os elementos podem ser sucessivamente removidos da raiz da heap, na ordem desejada.
   A heap pode ser representada como uma árvore (uma árvore binária com propriedades especiais) ou como um vetor. Para uma ordenação decrescente, deve ser construída uma heap mínima (o menor elemento fica na raiz). Para uma ordenação crescente, deve ser construído uma heap máxima (o maior elemento fica na raiz).
   By andrefelipeslv (padrão diferente)
   
### insertion_sort --> Algoritmo de ordenação por inserção
   O algoritmo de ordenação por inserção (insertion sort) compara determinado valor (a partir da segunda posição) com todos os valores anteriores e troca se algum valor anterior for maior que o valor da posição comparada.
   O laço interno garante que todos os valores anteriores a posição definida (2 - n) serão comparados. Enquanto o laço externo garante que o laço interno se repetirá a quantidade de vezes necessárias para que todos os valores tomem suas respectivas posições.
   
### merge_sort

### quick_sort --> Algoritmo de ordenação por divisão e conquista 
   No metodo quick sort, um valor 'pivô' é escolhido como valor inicial para a ordenação (geralmente é escolhido o primeiro ou ultimo valor). A partir dele, os elementos são comparados entre si e irão trocar de lugar até 'alcançarem' o pivô, onde serão organizados acima (maior) ou abaixo (menor) do que ele. Após a primeira execução, vão existir duas  partições - os valores menores e os valores maiores do que o pivô (que estará na sua posição correta). Recursivamente, serão escolhidos novos pivôs em ambos os lados até que todos os valores estejam ordenados.
   By arthuregood (padrão diferente)
   
### radix_sort

### selection_sort --> Algoritmo de ordenação por seleção
   O algoritmo de ordenação por seleção (selection sort) percorre o vetor em busca do menor valor. Em seguida transfere-o para a posição esperada.
   O laço interno busca o menor valor, o laço externo posiciona-o conforme esperado e garante qu eo laço externo se repita a quantidade de vezes necessárias para buscar o próximo menor valor até que todos estejam ordenados.  
   
### shellsort_sort --> Refinamento do método de inserção
   É um refinamento do método de inserção direta. O algoritmo difere do método de inserção direta pelo fato de no lugar de considerar o array a ser ordenado como um único segmento, ele considera vários segmentos sendo aplicado o método de inserção direta em cada um deles.  Basicamente o algoritmo passa várias vezes pela lista dividindo o grupo maior em menores. Nos grupos menores é aplicado o método da ordenação por inserção.
   By HelersonB

### radix_sort

### Timsort

###Gnome_sort
   Proposto pelo iraniano Hamid Sarbazi-Azad em 2000. Conhecido como “Stupid sort” por ser um algoritmo com uma logica muito simples. Um alemão chamado de Dick Grune mudou o nome do algoritmo para Gnome Sort em homenagem a um anão de jardim alemão. O Gnome Sort é baseado na técnica usada pelo duende de jardim alemão, basicamente, ele olha o vaso de flor próximo a ele e o anterior, se eles estão na ordem certa ele avança um vaso, caso contrário ele troca os jarros e volto um passo, Condições de parada: se não tem um jarro anterior ao atual, ele avança um passo, se não tem um jarro após o atual, está tudo organizado.





   
