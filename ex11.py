# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

number1 = int(input("Give the 1º number: "))
number2 = int(input("Give the 2º number: "))
number3 = float(input("Give the 3º number: "))

a = number1 * 2 + number2 / 2
b = number1 * 3 + number3
c = number3 ** 2

print(f"The results for your request are: {a}, {b}, {c}")
