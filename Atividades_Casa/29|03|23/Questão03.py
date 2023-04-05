try:
  numero = int(input("Digite um numero entre 0 e 1000  : "))
  if 0 < numero < 1000:
    valor = numero % 2
  
    if valor == 1 :
      print(f"O numero {numero} é impar")
  
    elif valor == 0 :
      dividido4 = numero % 4
      print(f"O numero {numero} é par")
      else:
         print("Não é divisivel por 4")
  else :
    print("Erro\nSelecione um numero valido.")
    

except ValueError:
  print("\nErro:\nSelecione um numero valido.")