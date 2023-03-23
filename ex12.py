#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

height = float(input("What is your high? "))

ideal_weight = (72.7 * height) - 58

print(f"Your ideal weight, based on your height, is {ideal_weight:.2f}")