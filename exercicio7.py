"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
de aumento."""

preco = int(input("digite um número: "))
desconto = preco-(preco*0.05)
aumento = preco+(preco*0.15)

print(f"o preço do seu produto é {preco}, seu valor com desconto é de {desconto} e de aumento {aumento}")
