from time import sleep
def start():
    import random
    from time import sleep

    def play_game():
            chances = 6
            digitadas = []

            letters_in_underline = ''
            for secret_world in secreto:
                letters_in_underline += '_'
            print(f'A PALAVRA É: {letters_in_underline}')

            while True:
                if chances == 6:
                    print('|-------| \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                         '----\n')
                if chances == 5:
                    print('|-------| \n'
                          '|      (_) \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                        '----\n')
                if chances == 4:
                    print('|-------| \n'
                          '|      (_) \n'
                          '|       |  \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                         '----\n')
                if chances == 3:
                    print('|-------| \n'
                          '|      (_) \n'
                          '|      /|  \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                         '----\n')
                if chances == 2:
                    print('|-------| \n'
                          '|      (_) \n'
                          '|      /|\  \n'
                          '|         \n'
                          '|         \n'
                          '|         \n'
                         '----\n')
                if chances == 1:
                    print('|-------| \n'
                          '|      (_) \n'
                          '|      /|\  \n'
                          '|      /- \n'
                          '|         \n'
                          '|         \n'
                         '----\n')

                letra = input('Digite uma LETRA: ')
                sleep(0.1)
                letra = letra.lower()

                if letra in digitadas:
                    print('                 ATENÇÂO!!')
                    sleep(0.5)
                    print('Você já digitou essa letra, tente novamente.')
                    sleep(0.8)

                if (letra not in secreto) and (letra not in digitadas) and (len(letra) == 1) and letra.isalpha() == True:
                    chances -= 1


                if letra.isalpha():
                    # inserindo a letra na lista DIGITADAS
                    digitadas.append(letra)
                    # retirando elementos repetidos da lista
                    digitadas = set(digitadas)
                    digitadas = list(digitadas)

                if letra.isalpha() == False:
                    print('                 ATENÇÂO!!')
                    sleep(0.5)
                    print('CARACTERE INVÁLIDO! Apenas permitido LETRAS.')
                    sleep(0.8)

                secreto_temporario = ''
                for letra_secreta in secreto:
                    if letra_secreta in digitadas:
                        secreto_temporario += letra_secreta
                    else:
                        secreto_temporario += '_'

                if len(letra) > 1:
                    print('                 ATENÇÂO!!')
                    sleep(0.5)
                    print('NÃO é PERMITIDO digitar mais de uma LETRA\n')
                    sleep(0.8)
                    print(f'A palavra secreta está assim: {secreto_temporario}')
                    print(f'      Você tem {chances} chances \n')
                    continue

                if secreto_temporario == secreto:
                    print('\n           PARABÉNS!!')
                    sleep(0.8)
                    print('Você VENCEU e ESCAPOU da FORCA!\n\n')
                    sleep(1)
                    print(f'A palavra secreta era {secreto.upper()}\n')
                    sleep(1)

                    play_again()

                else:
                    print(f'\nA palavra secreta está assim: {secreto_temporario}')

                if chances <= 0:
                    print('|-------| \n'
                          '|      (_) \n'
                          '|      /|\  \n'
                          '|      /-\ \n'
                          '|         \n'
                          '|         \n'
                         '----\n')
                    print('\n          ENFORCADO!!')
                    sleep(0.8)
                    print('Você perdeu! FORCA!\n\n')
                    sleep(1)
                    print(f'A palavra secreta era {secreto.upper()}\n')
                    sleep(1)

                    play_again()
                print(f'      Você tem {chances} chances \n')
    def play_again():
        play_again = input('Digite [1] para jogar novamente\n''Digite [2] para encerrar o jogo\n')
        if play_again == '1':
            sleep(0.5)
            start()
        elif play_again == '2':
            stop()
        else:
            print('\nOpção inválida, tente novamente!\n')
        while play_again != 1 or play_again != 2:
            play_again = input('Digite [1] para jogar novamente\n''Digite [2] para encerrar o jogo\n')
            if play_again == '1':
                sleep(0.5)
                start()
            elif play_again == '2':
                exit('Finalizando...')
            else:
                print('\nOpção inválida, tente novamente!\n')
    def stop():
        sleep(1)
        print('Create by José Gomes.')
        sleep(1)
        print('2022111510027@iesp.edu.br')
        sleep(1)
        print('Finalizando...')
        sleep(1)
        exit('Finalizado')
    def initial_sleep():
        sleep(1)
        print('Escolhendo palavra aleatória...\n')
        sleep(2)

    opção = 0
    chances = 6

    animais = ['formiga', 'elefante', 'girafa', 'passarinho', 'peixe', 'rato', 'coelho', 'cachorro', 'golfinho', 'abelha', 'leao', 'lobo', 'tigre', 'leopardo', 'zebra', 'porco', 'gato', 'boi', 'vaca', 'galinha', 'cobra', 'aranha', 'escorpiao']
    objetos = ['balao', 'caneca', 'celular', 'copo', 'computador', 'estojo', 'oculos', 'bolsa', 'garrafa', 'botao',  'agulha', 'anel', 'banco', 'binoculo', 'espada', 'frasco','navalha', 'spray', 'fita', 'nebulizador', 'tomada', 'livro', 'caderno']
    paises = ['brasil', 'alemanha', 'italia', 'argentina', 'frança', 'belgica', 'equador', 'venezuela', 'iraque', 'russia', 'chile', 'japao', 'china', 'argelia', 'bolivia', 'colombia','angola','espanha', 'haiti','jamaica','paraguai']
    comida = ['macarrao', 'feijao', 'arroz', 'milho', 'chocolate', 'doritos', 'biscoito', 'batata', 'hamburguer', 'sanduiche', 'salgadinho', 'farofa', 'iogurte', 'sushi', 'gelatina','pastel', 'achocolatado', 'brigadeiro', 'batata']
    aleatorio = animais + objetos + paises + comida

    ##menu##
    while opção != 6:

        print('-' * 18, 'Jogo da Forca', '-' * 18)
        ctg = input('''Qual categoria você vai escolher?\n
    Digite [1] para Animais 
    Digite [2] para Objetos 
    Digite [3] para Países 
    Digite [4] para Comida 
    Digite [5] para Tema Aleatório \n
Digite [6] para sair do Programa\n''')
        print('='*25)

        if ctg == '1':
            opção = 1
            print('A categoria escolhida foi [ANIMAIS]\n')
            animais = random.choice(animais)
            break

        elif ctg == '2':
            opção = 2
            print('A categoria escolhida foi [OBJETOS]\n')
            objetos = random.choice(objetos)
            break

        elif ctg == '3':
            opção = 3
            print('A categoria escolhida foi [PAÍSES]\n')
            paises = random.choice(paises)
            break

        elif ctg == '4':
            opção = 4
            print('A categoria escolhida foi [COMIDA]\n')
            comida = random.choice(comida)
            break

        elif ctg == '5':
            opção = 5
            print('A categoria escolhida foi [TEMA ALEATÓRIO]\n')
            aleatorio = random.choice(aleatorio)
            break

        elif ctg == '6':
            opção = 6
            break

        else:
            print('Essa opção é inválida, tente novamente.')
    ##fim-menu##

    if opção == 1:
        secreto = animais
        initial_sleep()
        play_game()

    if opção == 2:
        secreto = objetos
        initial_sleep()
        play_game()

    if opção == 3:
        secreto = paises
        initial_sleep()
        play_game()

    if opção == 4:
        secreto = comida
        initial_sleep()
        play_game()

    if opção == 5:
        secreto = aleatorio
        if secreto in animais:
            sleep(1)
            print('                   [ANIMAIS]\n')
        elif secreto in objetos:
            sleep(1)
            print('                   [OBJETOS]\n')
        elif secreto in paises:
            sleep(1)
            print('                   [PAÍSES]\n')
        elif secreto in comida:
            sleep(1)
            print('                   [COMIDA]\n')
        initial_sleep()
        play_game()

    if opção == 6:
        stop()
sleep(0.5)
start()