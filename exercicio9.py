"""Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros."""

real = int(input("digite o valor que você tem em sua carteira: "))
dolar = real/4.98
euro = real/5.43 


print(f"o valor da sua carteira {real} em dolar é {dolar:.2f} e em euro {euro:.2f}")