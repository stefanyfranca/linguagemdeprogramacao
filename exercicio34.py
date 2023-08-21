"""Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte

a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte."""

filmes = ["senhor dos anéis","Barbie","Cinderela","Moana", "Vingadores"]
jogos = ["CrossFire","Roblox","PUBG","Minecraft","Elden Ring"]
livros = ["Harry Potter","O Alquimista","O Código da Vinci","E o Vento Levou","O Senhor dos Anéis"]
esporte = ["futebol","volei","beisebal","hóquei","handbal"]
contador = 0

#a)
while contador != 2: 
    adicionar = input("digite um filme: ") 
    filmes.append(adicionar)
    adicionar = input("digite um jogo: ") 
    jogos.append(adicionar)
    adicionar = input("digite um livro: ") 
    livros.append(adicionar)
    adicionar = input("digite um esporte: ") 
    esporte.append(adicionar)
    contador += 1
    
print(filmes)
print(livros)
print(jogos)
print(esporte)

#b)
quatrolistas = ["filmes","livros","jogos","esporte"]

#c)
print(livros[1])

#d)
esporte.remove("senhor dos anéis")