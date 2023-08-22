"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

eleitores = int(input("digite o número de eleitores: "))
contA = 0
contB = 0
contC = 0
cont = 0
while cont != eleitores:
    print("a - Amoroso\n"+
    "b - Bino\n"+
    "c - Cardoso")
    candidato = input("digite seu candidato: ").upper()
    if candidato == "A":
        contA += 1
    if candidato == "B":
        contB += 1
    if candidato == "C":
        contC += 1
    cont += 1
    
print(f"votos para o candidato A: {contA}")
print(f"votos para o candidato B: {contB}")
print(f"votos para o candidato C: {contC}")