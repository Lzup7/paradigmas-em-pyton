try:
  genero = str(input("Por favor selecione seu genero. Masculino(M) Feminino(F) : ")).upper()
  
  if genero == "M" or genero == "F":   
   
    if (genero == "M" )   :
      print("Masculino")
    else: 
      print("Feminino") 
                                    
  else:
    print("\nErro:\nPor favor selecione um valor Valido (M) ou (F).")
      
    
except ValueError:
    print("\nErro:\nPor favor, selecione um valor valido.")