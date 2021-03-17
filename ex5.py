#m posto está vendendo combustíveis com a seguinte tabela de descontos:

#    Álcool: até 20 litros, desconto de 3% por litro
#    acima de 20 litros, desconto de 5% por litro
#
#    Gasolina:
#    até 20 litros, desconto de 4% por litro
#    acima de 20 litros, desconto de 6% por litro
#
#    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
# gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


tipoCombustivel = input("Digite o tipo do combustível: (A-álcool, G-gasolina): ")
qtdCombustivel = float(input("Digite a quantidade de combustível a ser abastecido: "))


if tipoCombustivel == "A" and qtdCombustivel <= 20:
    totalAPagar = (qtdCombustivel * 1.90)*0.97
elif tipoCombustivel == "A" and qtdCombustivel > 20:
    totalAPagar = (qtdCombustivel * 1.90)*0.95
elif tipoCombustivel == "G" and qtdCombustivel <= 20:
    totalAPagar = (qtdCombustivel * 2.5)*0.96
elif tipoCombustivel == "G" and qtdCombustivel > 20:
    totalAPagar = (qtdCombustivel * 2.5)*0.94

print(f"O total a pagar será de: R$ {round(totalAPagar,2)}")
