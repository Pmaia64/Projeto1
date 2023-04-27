#Jogo da Palavra secreta
palavra_secreta = 'developer'

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra. ')
        continue

    