"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá
receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser
informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser
conforme o exemplo abaixo:
a. Lojas Tabajara
b. Produto 1: R$ 2.20
c. Produto 2: R$ 5.80
d. Produto 3: R$ 0
e. Total: R$ 9.00
f. Dinheiro: R$ 20.00
g. Troco: R$ 11"""


while True:
    n = 1
    total = 0

    while True:
        preco = float(input("Produto em R$: "))
        n += 1
        total += preco
        if preco == 0:
            break

    print("Total: R$ {:.2f} ".format(total))
    dinheiro = float(input("Dinheiro: R$ "))
    print("Troco: R$ {:.2f}".format(dinheiro - total))


    reset = input("pressione R para reset, E para encerrar: ").upper()
    if reset == "R":
        continue
    else:           
        break