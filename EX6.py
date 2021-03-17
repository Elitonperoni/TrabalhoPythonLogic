#    Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                     Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qtdMacaAdquirida = float(input("Digite a quantia(Kg) de maçã adquirida: "))
qtdMorangoAdquirida = float(input("Digite  a quantia(Kg) de Morango adquirida: "))

if qtdMacaAdquirida <= 5:
    precoMaca = 1.8
elif qtdMacaAdquirida > 5:
    precoMaca = 1.5

if qtdMorangoAdquirida <= 5:
    precoMorango = 2.5
elif qtdMorangoAdquirida > 5:
    precoMorango = 2.2

qtdTotalAdquirida = qtdMacaAdquirida + qtdMorangoAdquirida
totalPagar = (qtdMacaAdquirida * precoMaca) + (qtdMorangoAdquirida * precoMorango)

if totalPagar >= 25 or qtdTotalAdquirida >= 8:
    totalPagar = totalPagar*0.9

#Imprime o valor a pagar
print("O total a pagar será de: R$ ", totalPagar)
