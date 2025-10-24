def pesquisa_binaria(lista, item):
    baixo = 0 # A posição mais baixa da lista é a posição 0
    alto = len(lista) - 1 # - - Anotação 01 - -

    while baixo <= alto: # Enquanto não reduzir as possibilidades a 1 elemento a procura vai se repetir

        meio = (baixo + alto) // 2 # Vê quem é o número do meio
        chute = lista[meio] # Pega o número na posição meio da lista e põe na variável chute

        if chute == item: # Se o chute for o item, ele retorna o resultado
            return meio

        if chute > item: # Se não encontrou ainda e o número do meio (chute) era maior que o item, o do meio vira o mais alto
            alto = meio - 1 # - - Anotação 02 - -

        else: # Se o chute for muito baixo, o do meio vira o mais baixo
            baixo = meio + 1 # - - Anotação 02 - -
    return None # Se nem for contado while, ou seja, o valor não existir na lista, retorna none

minha_lista = [1, 3, 5, 7, 9] # Essa é minha lista de itens

# Nessa parte inteira eu chamo os itens para saber as suas posições na lista
print(pesquisa_binaria(minha_lista, 1))
print(pesquisa_binaria(minha_lista, 7)) # Os argumentos que eu envio para a função são a lista inteira e o número que quero saber a posição
print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

# -- Nota Extra --
# Bucket é o nome do espaço que se da às listas, para armazenas os números, seria aquele quadradinho com cada indicie
# Um conceito muito importante é saber Log a base 2 de tudo, pois é assim que os binários funcionam
    # Usando Log2 de qualquer número sabemos quantas pesquisas precisamos fazer para encontrar aquele número
    # Log2 é basicamente "Quantas vezes preciso multiplicar por 2 para chegar aquele número?", ou seja, o expoente de 2
    # Para encontrar basta apenas fatorar o número que quer saber de 2 em 2

# - - Anotação 01 - -
# O índice máximo de uma lista é sempre (tamanho da lista - 1).
    # Isso porque os índices começam em 0, então:
    #   - Se a lista tem 5 (quantidade) elementos então os índices válidos vão de 0 até 4.
    #   - Por isso precisamos subtrair 1,
    #   - Senão tentaríamos acessar lista[5], que não existe, pois len(lista) retorna a quantidade de itens e não o indicie.

# - - Anotação 02 - -
# [alto = meio - 1]
# Se o número do meio (chute) for MAIOR que o item procurado:
    # Significa que o item só pode estar à esquerda.
    # Por isso, ajustamos 'alto' para meio - 1,
    # Descartando o valor do meio e toda a parte à direita dele.
    # Colocamos o "-" justamente para não contar novamente esse do meio que já foi descartado pegando apenas os inferiores
    # Tipo, numa lista de 8 valores, o do meio é o 4, você já sabe que não é ele, reduzimos o meio para o 2 e o 4 já náo é mais contado (-1)
    # O 4 não é mais contado porque já verificamos se é ele na primeira redução

# [baixo = meio + 1]
# Se o número do meio (chute) for MENOR que o item procurado:
    # Significa que o item só pode estar à direita.
    # Por isso, ajustamos 'baixo' para meio + 1,
    # Descartando o valor do meio e toda a parte à esquerda dele.
    # Colocamos o "+" justamente para não contar novamente esse do meio que já foi descartado pegando apenas superiores
    # Numa lista de 8 valores, sabendo que o 4 não era o valor, ele vai subir para 6 e o 4 não vai ser mais considerado, pois sabemos que não é ele (+1)