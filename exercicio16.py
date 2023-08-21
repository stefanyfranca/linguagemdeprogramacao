"""Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão"""

temperatura = float(input("digite uma temperatura: "))
unidade = int(input("você deseja converter sua temperatura para fahrenheit(1) ou para celsius(2)"))

if unidade == 1:
    fahrenheit = (temperatura * 1.8)+32
    print(f"a temperatura em fahrenheit é {fahrenheit}")
if unidade == 2:
    celsius = (temperatura-32)*5/9
    print(f"a temperatura em celsius é {celsius}")

