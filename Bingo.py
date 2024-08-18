''' Estrutura para guardar os números sorteados em um bingo'''
bingo_numeros = {}

#adiciona números sorteados a cada rodada

while True:

    rodada = int(input("Digite o número da rodada: "))
    numero_sorteado = int(input("Digite o número sorteado: "))

    if rodada not in bingo_numeros:
        bingo_numeros[rodada] = set()

    # Verifica se o número já foi sorteado nesta rodada ou em qualquer rodada anterior
    ja_sorteado = False
    for numeros in bingo_numeros.values():
        if numero_sorteado in numeros:
            ja_sorteado = True
            break

    if ja_sorteado:
        print("Este número já foi sorteado. Tente novamente.")
    else:
        bingo_numeros[rodada].add(numero_sorteado)
        print(f"Número {numero_sorteado} adicionado na rodada {rodada}.")

    print("\nNúmeros sorteados até agora:")
    for rodada, numeros in bingo_numeros.items():
        print(f"Rodada {rodada}: {sorted(numeros)}")

    continuar = input("\nDeseja continuar sorteando? (s/n): ")
    if continuar.lower() != 's':
        break
