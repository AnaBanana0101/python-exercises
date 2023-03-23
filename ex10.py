#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = int(input("What is the temperature in Celsius? "))

fahrenheit = celsius * 1.8 + 32

print(f"The temperature in Fahrenheit is {fahrenheit:.2f}")