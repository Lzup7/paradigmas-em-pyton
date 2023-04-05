try:
  nota1 = float(input("Qual sua primeira nota: "))
  nota2 = float(input("Qual sua segunda nota: "))
  result = (nota1 + nota2 ) / 2
  if 0< result <= 10:

      if result >= 6 and result < 10 :
        print(f"Sua media é {result:.1f}\nFoi aprovado")
        
      elif result < 6:
        print(f"Sua media é {result:.1f}\nFoi reprovado")
        
      elif result == 10 :
       print(f"Sua media é {result:.1f}\nFoi aprovado com distinsão ")
  else:
    print("Ocorreu um erro\nSão apenas permitidos numeros de 0 a 10")

except ValueError:
  print("Ocorreu um erro\nSão apenas permitidos numeros de 0 a 10")
  