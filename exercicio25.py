"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações"""

while True:
    nome = input("digite seu nome: ").upper()
    senha = input("digite sua senha: ").upper()
    if senha == nome:
        print("senha igual ao usuário, digite novamente")
    else:
        break