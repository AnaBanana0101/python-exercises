#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalha por dia? "))

salario = (ganho_hora * horas_trabalhadas) * 20 

print(f"O seu salário mensal será de R${salario:.2f}")