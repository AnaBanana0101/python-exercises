# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# # comprar apenas latas de 18 litros;
# # comprar apenas galões de 3,6 litros;
# # misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# # Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math 

metros = int(input("Digite a quantidade de metros quadrados a serem pintados: "))

litros = metros / 6
litros_folga = litros * 1.1

precoL = 80.0
precoL2 = 25
capacidadeL = 18
capacidadeL2 = 3.6

latas = litros / capacidadeL #Latas de 18L
latas2 = litros / capacidadeL2 #Latas de 3,6L
qtd_latas_g = litros_folga // capacidadeL


latas = math.ceil(latas)
latas2 = math.ceil(latas2)


litros_folga_faltando = litros_folga - (qtd_latas_g * capacidadeL)
qts_latas_p = math.ceil(litros_folga_faltando / capacidadeL2)

total = (latas * precoL) #Latas de 18L
total2 = (latas2 * precoL2)  # Latas de 3,6L

conta_mix = (qtd_latas_g * precoL) + (qts_latas_p * precoL2)


print(f"O total de latas de 18L a serem compradas é de {latas}, no valor de R${total:.2f}")
print(f"O total de latas de 18L a serem compradas é de {latas2}, no valor de R${total2:.2f}")
print(f"Na compra de latas de tamanhos diferentes serão necessarios {qtd_latas_g} da lata e {qts_latas_p}, com um total de R${conta_mix:.2f} ")


