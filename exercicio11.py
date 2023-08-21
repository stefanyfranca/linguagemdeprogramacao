"""Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
ao final mostrar seu nome e salário final calculado."""

nome = input("digite seu nome: ")
horas = float(input("digite seu número de horas trabalhadas: "))
valordahora = float(input("digite o valor das suas horas trabalhadas: "))

salario = horas*valordahora
inss = salario-(salario*0.02)

print(f"olá {nome}, seu salário bruto é de {salario}, mas devido aos descontos do INSS vocÊ receberá {inss}")

