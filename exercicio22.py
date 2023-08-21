"""Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada."""
lista = []
i=0
while i != 1000:
    numero = int(input("digite um número: "))
    lista.append(numero)
    i += 1
    if numero == 1000:
        print(f"a soma dos números digitados é {sum(lista)- 1000}, foram digitados {i} números")

