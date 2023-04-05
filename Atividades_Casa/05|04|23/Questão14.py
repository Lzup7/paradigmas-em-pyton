while True:
  try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    if 9 <= media <= 10 :
      mediaF = "A"
      print(f"Você tirou {mediaF}, Você foi aprovado.")
      break
    elif 7.5 <= media < 9 :
      mediaF = "B"
      print(f"Você tirou {mediaF}, Você foi aprovado.")
      break
    elif 6 <= media < 7.5 :
      mediaF = "C"
      print(f"Você tirou {mediaF}, Você foi aprovado.")
      break
    elif 4 <= media < 6 :
      mediaF = "D"
      print(f"Você tirou {mediaF}, Você foi reprovado.")
      break
    elif 0 <= media < 4 :
      mediaF = "E"
      print(f"Você tirou {mediaF}, Você foi reprovado.")
      break
    else: 
      print("\nErro:\nDigite um valor valido:\n")
  except:
    print("\nErro:\nDigite um valor valido:\n")
  