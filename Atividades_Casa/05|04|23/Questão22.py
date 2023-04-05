try:
  numero = int(input("Digite um numero entre 0 e 1000  : "))
  if 0 < numero < 1000:
    valor = numero % 2
  
    if valor == 1 :
      print(f"O numero {numero} é impar")
  
    elif valor == 0 :
      
      print(f"O numero {numero} é par")
      
  else :
    print("Erro\nSelecione um numero valido.")
    

except ValueError:
  print("\nErro:\nSelecione um numero valido.")