tuplas = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
novo_valor = 100

# Mudando o último elemento de cada tupla
for i in range(len(tuplas)):
    tupla = tuplas[i]
    # Substituindo o último elemento da tupla
    tuplas[i] = tupla[:-1] + (novo_valor,)
print(tuplas)

