"""Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos."""

idade = int(input("digite sua idade: "))
tempo = int(input("digite quantos anos já contribuiu: "))

if idade >= 65:
    print(f"sua idade é {idade}, você já pode se aposentar!")
elif tempo >= 30:
    print(f"seu tempo de contribuição é de {tempo}, você já pode se aposentar!")
elif tempo >= 25 and idade >= 60:
    print(f"seu tempo de contribuição é de {tempo} e sua idade é {idade}, você já pode se aposentar!")
else:
    print(f"sua idade é {idade} e seu tempo de contribuição é de {tempo}, você não pode se aposentar!")