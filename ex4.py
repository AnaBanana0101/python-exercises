#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Nota do 1º semestre: "))
nota2 = float(input("Nota do 2º semestre: "))
nota3 = float(input("Nota do 3º semestre: "))
nota4 = float(input("Nota do 4º semestre: "))

media = nota1 + nota2 + nota3 + nota4 / 4

print(f"A média das notas é de {media:.2f}")