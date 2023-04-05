try:
  while True:
    print("Selecione o preço dos produtos abaixo:")
    produto1 = float(input("produto 1 : R$"))
    produto2 = float(input("produto 2 : R$"))
    produto3 = float(input("produto 3 : R$"))
    
    if produto1 < produto2 and produto1 < produto3:
      print(f"O produto 1 é o mais em conta")
    elif produto2 < produto1 and produto2 < produto3 :
      print(f"O produto 2 é o mais em conta")
    elif produto3 < produto1 and produto3 < produto2:
      print(f"O produto 3 é o mais em conta")
      break
    else:
      print("Erro\nSelecione um valor valido:")
except :
  print("Erro\nSelecione um valor valido")
  