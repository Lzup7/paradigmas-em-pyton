try:
  nota1 = float(input("Qual sua primeira nota: "))
  nota2 = float(input("Qual sua segunda nota: "))
  
  if (nota1 <= 10 and nota1 > 0) and (nota2 <= 10 and nota2 > 0):
    
    
      result = (nota1 + nota2 ) / 2
      
      if result >= 6 and result < 10 :
        print(f"Sua media é {result:.1f}\n parabens vc passou")
        
      elif result < 6:
        print(f"Sua media é {result:.1f}\n F no chat. Better luck next time")
        
      elif result == 10 :
       print(f"Sua media é {result:.1f}\nCarai tu é foda ein ")
      else:
        print("Digite a nota certa desgraça")
    


  
  
except ValueError:
  print("Ocorreu um erro\nSão apenas permitidos numeros de 0 a 10")
  