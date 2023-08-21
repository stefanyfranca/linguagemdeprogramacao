"""Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 números.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero)."""

print("a.Soma de 2 números \n"+
    "b.Diferença entre 2 números\n"+
    "c.Produto entre 2 números \n"+
    "d.Divisão entre 2 números \n")
escolha = input("digite sua escolha: ").upper()

if escolha == "A":
    numero1 = int(input("digite o primeiro número: "))
    numero2 = int(input("digite o segundo número: "))
    soma = numero1+numero2
    print(f"a soma dos números {numero1} e {numero2} é {soma}")
if escolha == "B":
    numero1 = int(input("digite o primeiro número: "))
    numero2 = int(input("digite o segundo número: "))
    if numero1 > numero2:
        diminuir = numero1-numero2
        print(f"a divisão dos números {numero1} e {numero2} é {diminuir}")
    if numero2 > numero1:
        diminuir = numero2-numero1
        print(f"a divisão dos números {numero2} e {numero1} é {diminuir}")
if escolha == "C":
    produto = numero1*numero2
    print(f"a produto dos números {numero1} e {numero2} é {produto}")
if escolha == "D":
    if numero2 < 0.1:
        print("numero inválido")

    else:
        divisao = numero1/numero2
        print(f"a produto dos números {numero1} e {numero2} é {divisao}")