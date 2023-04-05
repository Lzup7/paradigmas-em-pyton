try:

  while True:
    numero1 = int(input("Digite o primeiro numero:"))
    numero2 = int(input("Digite o segundo numero numero:"))
    numero3 = int(input("Digite o terceiro numero numero:"))
    
    if numero1 > numero2 and numero1 > numero3:
      print(f"O numero {numero1} é maior que {numero2} e {numero3}")
    elif numero2 > numero1 and numero2 > numero3 :
      print(f"O numero {numero2} é maior que {numero1} e {numero3}")
    elif numero3 > numero2 and numero3 > numero1:
      print(f"O numero {numero3} é maior que {numero1} e {numero2}")
      break
    else:
     print("\nErro!\nSelecione numeros distintos:\n")
except :
 print("\nErro!\nSelecione um valor valido.")
  
