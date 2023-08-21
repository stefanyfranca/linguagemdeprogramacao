"""Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores."""

maior = 0
menor = 9999999999999999999999
valores = []
opcao = True

while opcao:
    numero = int(input("digite um valor: "))
    if numero > maior:
        maior = numero
        print(f"maior número: {maior}")
        print(f"menor número: {menor}")
    if numero < menor:
        menor = numero
        print(f"menor número: {menor}")
        print(f"maior número: {maior}")
    valores.append(numero)
    print(valores)
    opcao = input("deseja continuar (s ou n): ").upper()
    if opcao == "S":
        opcao == True
    else:
        break