"""Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';"""

nome = input("digite seu noma: ")
idade = int(input("digite sua idade: "))
salario = float(input("digite seu salário"))
sexo = input("digite seu sexo (f ou m)").upper()
print("s -solteiro\n" +
    "c - casado\n"+
    "v - viúvo\n"+
    "d - divorciado\n")
estado = input("digite seu estado civil: ").upper()
quantidade = len(nome)

if quantidade <= 3:
    print(f"nome inválido, seu nome foi {nome}")
else:
    print(f"nome válido, seu nome foi {nome}")
if idade < 0 or idade > 150:
    print(f"idade inválida, sua idade foi {idade}")
else:
    print(f"idade válida, sua idade foi {idade}")
if salario < 0:
    print(f"salário inválido, seu salário foi {salario}")
else:
    print(f"salário válido, seu salário foi {salario}")
if sexo == "F" or sexo == "M":
    print(f"seu sexo é {sexo}")
else:
    print("sexo inválido")
if estado == "S" or "C" or "V" or "D":
    print("estado cívil válido")

