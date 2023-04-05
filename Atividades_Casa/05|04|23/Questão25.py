
print("Selecione Sim(s) ou Não(n) para responder as perguntas: ")

perguntas = [
    "Telefonou para a vitima?: ",
    "Esteve no local do crime?: ",
    "Mora perto da vitima?: ",
    "Devia para a vitima?: ",
    "Já trabalhou com a vitima?: "
]
resposta = 0

for status in perguntas:
    resposta += (input(status) == "s" )

if resposta == 5:
    print("Assassino")

elif resposta >= 3:
    print("Cúmplice")

elif resposta == 2:
    print("Suspeito")

else:
    print("Inocente")