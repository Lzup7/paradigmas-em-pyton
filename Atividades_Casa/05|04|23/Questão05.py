try:
  nota1 = float(input("Qual sua primeira nota: "))
  nota2 = float(input("Qual sua segunda nota: "))
  
  if (nota1 <= 10 and nota1 > 0) and (nota2 <= 10 and nota2 > 0):
    
    
      result = (nota1 + nota2 ) / 2
      
      if result >= 6 and result < 10 :
        print(f"Sua media é {result:.1f}\nParabens você passou")
        
      elif result < 6:
        print(f"Sua media é {result:.1f}\nAluno não foi aprovado")
        
      elif result == 10 :
       print(f"Sua media é {result:.1f}\nParabens aprovado com distinsão ")
      else:
        print("Digite as informações corretamente")

except ValueError:
  print("Ocorreu um erro\nSão apenas permitidos numeros de 0 a 10")
  
