import math
saque = int(input("Quanto vai sacar: "))
nota100 = saque / 100
nota100_quantia = math.floor(nota100)
resto_nota100 = (nota100 - nota100_quantia) * 100

nota50 = resto_nota100 / 50
nota50_quantia = math.floor(nota50)
resto_nota50 = (nota50 - nota50_quantia) * 50

nota10 = resto_nota50 / 10
nota10_quantia = math.floor(nota10)
resto_nota_10 = (nota10 - nota10_quantia) * 10

nota5 = resto_nota_10 / 5
nota5_quantia = math.floor(nota5)
nota1 = (nota5 - nota5_quantia) * 5

print(f"Notas de 100: {nota100_quantia} \nNotas de 50: {nota50_quantia}\nNotas de 10: {nota10_quantia}")