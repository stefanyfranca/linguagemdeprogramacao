"""Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”"""

temperatura = float(input("digite a temperatura atual: "))

if temperatura <= 15:
    print(f"a {temperatura} é considerada fria!")
if temperatura > 15 or temperatura <= 21:
    print(f"a {temperatura} é considerada agradável!")
if temperatura > 21:
    print(f"a {temperatura} é considerada quente!")