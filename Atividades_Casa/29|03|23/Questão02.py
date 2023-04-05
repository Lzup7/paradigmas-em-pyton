try:
  genero = str(input("Por favor selecione seu genero. Masculino(M) Feminino(F) : ")).upper()
  
  if genero == "M" or genero == "F":   
    idade = int(input("Por favor selecione sua idade : "))    
    if 1 <= idade and 116 >= idade :
       if (genero == "M" and idade >= 65) or (genero == "F" and idade >= 60)  :
          print(f"\nVocê tem {idade} anos.\nJa pode se aposentar")
       else: 
          print(f"\nVocê tem {idade} anos.\nNão pode se aposentar") 
                                    
    else:
            print("\nErro:\nPor favor, selecione uma idade valida") 
  else:
    print("\nErro:\nPor favor selecione um valor Valido (M) ou (F).")
      
    
except ValueError:
    print("\nErro:\nPor favor, selecione um valor valido.")