"Faça um Programa que peça um número e informe se o número "
"é inteiro ou decimal. Dica: utilize uma função de arredondamento."

num1 = float(input("Digite um número: "))
num1Arredondado = round(num1)

if num1 != num1Arredondado:
    print("O número digitado é decimal")
else:
    print("O número digitado é inteiro")

