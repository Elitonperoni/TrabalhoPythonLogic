#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

("Digite 1 para responder SIM, e digite 2 para responder NÃO ")
pergTelefonou = int(input("Telefonou para a vítima?: "))
pergEsteveLocCrime = int(input("Esteve no local do crime?: "))
pergMoraPertoVitima = int(input("Mora perto da vítima?: "))
pergDeviaVitima = int(input("Devia para a vítima?: "))
pergTrabComVitima = int(input("Já trabalhou com a vítima?: "))

resultado = pergTelefonou + pergEsteveLocCrime + pergMoraPertoVitima + pergTrabComVitima + pergDeviaVitima

if resultado <=1:
    print("Inocente")
elif resultado == 2:
    print("Suspeita")
elif resultado >= 3 and resultado <=4:
    print("Cúmplice")
elif resultado >= 5:
    print("Assassina")

