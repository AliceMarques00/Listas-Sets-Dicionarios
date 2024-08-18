'''Exemplo de imagem (3x3) com valores RGB'''
imagem = [
    [(255.0, 0.0, 0.0), (0.0, 255.0, 0.0), (0.0, 0.0, 255.0)],
    [(255.0, 255.0, 0.0), (255.0, 0.0, 255.0), (0.0, 255.0, 255.0)],
    [(128.0, 128.0, 128.0), (64.0, 64.0, 64.0), (192.0, 192.0, 192.0)]
]

''' Processamento para transformar a imagem em tons de cinza'''
for i in range(len(imagem)):
    for j in range(len(imagem[i])):
        r, g, b = imagem[i][j]
        media = (r + g + b) / 3.0
        imagem[i][j] = (media, media, media)
'''Exibindo a imagem processada'''
for linha in imagem:
    print(linha)
