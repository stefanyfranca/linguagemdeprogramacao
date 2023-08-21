"""Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos."""

nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))

if nota1 > 5 or nota2 > 5 or nota3 > 10 or nota1 < 0 or nota2 < 0 or nota3 < 0:
    print("nota inválida")
else:
    media = (nota1+nota2+nota3)/3
    print(f"sua média é {media}")

