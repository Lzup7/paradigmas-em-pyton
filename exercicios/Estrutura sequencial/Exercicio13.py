sexo = str(input("Qual o seu sexo? masculino(m) femenino(f) : "))
altura = float(input("Qual a sua altura : "))
pesoM = (72.7 * altura) - 58
pesoF = (62.1 * altura) - 44.7

if sexo == "f":
 print(f"O seu peso ideal seria {pesoF:.1f}kg.")
else:
 if sexo == "m": 
    print(f"O seu peso ideal seria {pesoM:.1f}kg.")


print("tchau")