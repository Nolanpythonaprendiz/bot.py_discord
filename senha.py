import random
def senha():
    Caracteres = 'abcdefghijklmnopABCDEFGHIJKLMNOP1234567890!@#$%&'

    Tamanho = 10


    Senha = ''


    for i in range(Tamanho):
        Letra = random.choice(Caracteres)
        Senha += Letra

    print(Senha)
    return Senha