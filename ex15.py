# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

ganho_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalha por dia? "))

salario_bruto = (ganho_hora * horas_trabalhadas) * 20 
desc_ir = salario_bruto * 0.11
desc_inss = desc_ir * 0.08
desc_sindicato = desc_inss * 0.05

salario_liquido = salario_bruto - desc_inss - desc_ir - desc_sindicato

print(f"O seu salário bruto mensal será de R${salario_bruto:.2f}, o desconto do imposto de renda será de R${desc_ir:.2f}, o do INSS será de {desc_inss:.2f} e o do sindicato será de R${desc_sindicato:.2f}.\nO salario líquido no final será de R${salario_liquido:.2f}")