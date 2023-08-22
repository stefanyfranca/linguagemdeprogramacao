""") Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero."""
while True:
    eleitores = 0 
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    candidato4 = 0
    nulo = 0
    branco = 0

    print("1- candidato 1\n"+
        "2-candidato 2\n"+
        "3-candidato 3\n"+
        "4-candidato 4\n"+
        "5-brancos\n"+
        "6-nulos\n")

    opcao = int(input("digite seu voto:"))
                    
    if opcao == 1:
        candidato1 += 1
    if opcao == 2:
        candidato2 += 1
    if opcao == 3:
        candidato3 += 1
    if opcao == 4:
        candidato4 += 1
    if opcao == 5:
       branco += 1
    if opcao == 1:
      nulo += 1
    else:
        print("fim de jogo")
    eleitores += 1

print(f"votos em branco: {branco}")
print(f"votos nulos: {nulo}")
print(f"porcentagem dos votos {eleitores}")
