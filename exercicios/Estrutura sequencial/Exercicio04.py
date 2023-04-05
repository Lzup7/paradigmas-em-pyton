nome = str(input("Qual o seu nome: "))
nota1 = float(input("Qual sua 1*nota: "))
nota2 = float(input("Qual sua 2*nota: "))
nota3 = float(input("Qual sua 3*nota: "))
nota4 = float(input("Qual sua 4*nota: "))

result = (nota1 + nota2 + nota3 + nota4) / 4

if result >= 6:
  print(f"{nome} Sua media é {result}\n parabens vc passou")
else:
  print(f"{nome} Sua media é {result}\n F no chat. Better luck next time")
