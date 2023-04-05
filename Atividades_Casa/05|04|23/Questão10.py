
while True:
 try:
    turno = str(input("Qual o seu turno?\nM-matutino ou V-Vespertino ou N- Noturno.\n: ")).upper()
    turnos = "MVN"
    if turno in turnos:
      if turno == "M":
       print(f"Bom dia")
      elif turno == "V":
        print("Boa tarde")
      else:
        print(f"Boa noite")
      break
    else:
      print("\nErro!\nDigite um valor valido:\n")
 except:
   print("\nErro!\nDigite um valor valido:\n")
   