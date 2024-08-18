#      (nome,  hp,      golpe,          forçaGolpe)
cartas = [
    ("Pikachu", 35, "Choque do Trovão", 40),
    ("Charizard", 78, "Lança-Chamas", 90),
    ("Bulbasaur", 45, "Folha Navalha", 55),
    ("Squirtle", 44, "Jato de Água", 50)
]

# Adicionar 10 de HP a cada carta
for i in range(len(cartas)):
    nome, hp, golpe, forcaGolpe = cartas[i]
    cartas[i] = (nome, hp + 10, golpe, forcaGolpe)

# Modificar o HP de uma carta (modificar a primeira carta como exemplo)
cartas[0] = (cartas[0][0], cartas[0][1] + 5, cartas[0][2], cartas[0][3])

# Encontrar a carta com o maior HP
carta_mais_forte = cartas[0]
for carta in cartas:
    if carta[1] > carta_mais_forte[1]:
        carta_mais_forte = carta

# Encontrar o golpe mais forte
golpe_mais_forte = cartas[0]
for carta in cartas:
    if carta[3] > golpe_mais_forte[3]:
        golpe_mais_forte = carta

print("Carta com o maior HP:", carta_mais_forte)
print("Carta com o golpe mais forte:", golpe_mais_forte)
