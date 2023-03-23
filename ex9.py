#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

temperature = float(input("What the temperature in Fahrenheint? "))

celsius = 5 * ((temperature - 32) / 9)

print(f"The temperature converted in Celsius is {celsius:.1f}")