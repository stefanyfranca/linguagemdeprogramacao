"""Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo."""

from random import randint
cont = 0
while True:
    n = int(input('Digite o seu número: '))
    a = ' '
    while a not in 'PI':
        a = input('Escolha par ou ímpar [P/I]: ').upper()
    c = randint(0, 10)
    if (n + c) % 2 == 0:
        if a == 'P':
            print(f'VENCEU. Você escolheu {n}, o computador {c}. A soma é {c + n}')
        else:
            print(f'PERDEU. Você escolheu {n}, o computador {c}. A soma é {c + n}')   
            break
    if (n + c) % 2 != 0:
        if a == 'I':
            print(f'VENCEU. Você escolheu {n}, o computador {c}. A soma é {c + n}')
        else:
            print(f'PERDEU. Você escolheu {n}, o computador {c}. A soma é {c + n}')
            break
    cont += 1
print(f'Você venceu {cont} vezes')