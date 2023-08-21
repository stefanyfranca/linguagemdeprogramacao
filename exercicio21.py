"""Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso"""

valor1 = int(input("digite o valor1: "))
valor2 = int(input("digite o valor2: "))

print("a. Somar\n"+
    "b. Multiplicar\n"+
    "c. Maior\n"+
    "d. Menor\n"+
    "e. Sair do programa\n")
opcao = input("digite sua opção: ").upper()

if opcao == "A":
    soma = valor1+valor2
    print(f"sua soma é de {soma}")
if opcao == "B":
    multiplicar = valor1*valor2
    print(f"sua multiplicação é de {multiplicar}")
if opcao == "C":
    if valor1 > valor2:
        maior = valor1
        print(f"o maior é o valor1 = {valor1}")
    if valor2 > valor1:
        maior = valor2
        print(f"o maior é o valor2 = {valor2}")
if opcao == "D":
    if valor1 < valor2:
        menor = valor1
        print(f"o menor é o valor1 = {valor1}")
    if valor2 < valor1:
        menor = valor2
        print(f"o menor é o valor2 = {valor2}")
if opcao == "E":
    print("você está fora do programa!")