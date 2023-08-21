"""Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7"""

altura = float(input("digite sua altura: "))
print("h - homens \n" +
      "m - mulheres")
sexo = input("digite seu sexo: ").upper()


if sexo == "H":
    homens = (72.7 * altura) - 58
    print(f"seu peso ideal é: {homens}")
if sexo == "M":
    mulheres= (62.1 * altura) - 44.7
    print(f"seu peso ideal é: {mulheres}")