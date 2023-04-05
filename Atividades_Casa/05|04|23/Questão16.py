try:
  import math
  A = float(input("Digite a letra A: "))
  if A == 0:
      print("Valor Invalido")
  else:
      B = float(input("Digite a letra B: "))
      C = float(input("Digite a letra C: "))
  
  delta = (B ** 2) - (4 * A * C)
  
  if delta < 0:
          print("A equação não possui raizes reais")
  else:
      x1 = (-B + math.sqrt(delta)) / 2 * A
      x2 = (-B - math.sqrt(delta)) / 2 * A
  if delta == 0:
          print(f"Possui Uma Raiz real:{x1} ")
  else:
          print(f"Possui Duas raizes reais, x1: {x1}\nx2: {x2}")
except:
  print("Erro\nSelecione um valor valido.")