try:
  print("Digite 3 lados de um triangulo:")
  lado1 = float(input("primeiro Lado: "))
  lado2 = float(input("segundo Lado: "))
  lado3 = float(input("terceiro Lado: "))
  if ((lado1 + lado2)>= lado3) or ((lado3 + lado2)>= lado1) or ((lado1 + lado3)>= lado2): 
   if lado1 == lado2 == lado3:
     print("É um triangulo Equilatero.")
   elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
      print("É um triangulo Isósceles.")
   elif not lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
      print("É um triangulo Escaleno.")
    
  else:
   print("\nErro\nDigite um valor valido")
except:
  print("\nErro\nDigite um valor valido")
