"""Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo
pelo teclado e mostra na tela o seu tipo de dado."""

a = int(input("digite um número: "))
b = int(input("digite um número: "))

soma = a+b
tipo = type(soma)
print(f"a soma de a+b {soma} e seu tipo é {tipo}")