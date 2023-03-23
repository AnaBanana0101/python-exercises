# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

height = float(input("What is your high? "))

ideal_weight_man = (72.7 * height) - 58
ideal_weight_woman = (62.1 * height) - 44.7

print(f"Your ideal weight, based on your height, is {ideal_weight_woman:.2f} for womans and {ideal_weight_man:.2f} for mans.")