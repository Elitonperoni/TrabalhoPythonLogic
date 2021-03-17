"Faça um Programa que peça um número inteiro e determine se ele é par ou impar."
"Dica: utilize o operador módulo (resto da divisão)."

num1 = int(input("Digite um número inteiro: "))
resultado = num1 % 2
if resultado == 0:
    print("O número digitado é par")
else:
    print("O número digitado é ímpar")