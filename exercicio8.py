""" Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²."""

largura = float(input("digite a largura da sua parede: "))
altura = float(input("digite a altura da sua parede: "))

area = largura*altura
tinta = area/2

print(f"sua parede tem uma área de {area}m², para pinta-la você precisará de {tinta} baldes de tinta")