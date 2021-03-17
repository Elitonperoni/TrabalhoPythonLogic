#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele "
#deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:"
#  par ou ímpar;
#  positivo ou negativo;
#  inteiro ou decimal.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar: (x | / | + | - ): ")

## Operação
if operacao == "x":
    resultado = num1*num2
elif operacao == "/":
    resultado = num1/num2
elif operacao == "+":
    resultado = num1+num2
elif operacao == "-":
    resultado = num1-num2

## Define Ímpar ou Par
parImpar = resultado % 2
if parImpar == 0:
    resultadoParImpar = "Par"
else:
    resultadoParImpar=" Ímpar"

## Define Positivo ou Negativo
if resultado < 0:
    maiorMenorZero = "Negativo"
else:
    maiorMenorZero = "Positivo"

##Define Inteiro ou Decimal
inteiroDecimal = round(resultado)
if inteiroDecimal != resultado:
    resultadoInteiroDecimal = " Decimal "
else:
    resultadoInteiroDecimal = "Inteiro"

#Imprime o resultado final
print("O resultado da operação é ", resultado,", este número é ", resultadoParImpar, " , ", maiorMenorZero," e ", resultadoInteiroDecimal)




