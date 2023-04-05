try:
  
  idade = int(input("Qual sua idade : "))

  if 1 <= idade and 116 >= idade:
    if 18 <= idade and  70 > idade:
     print(f"Você possui {idade} anos.\nSeu voto é obrigatorio.")
    elif (16 <= idade and 17 >= idade) or (70 <= idade ):
      print(f"Você possui {idade} anos.\nSeu voto não é obrigatorio.")
    else:
       print(f"Você possui {idade} anos.\nVocê não vota.")
     

  else:
    print("\nErro:\nPor favor, selecione uma idade valida") 


except ValueError :
  print("\nErro:\nPor favor, selecione uma idade valida")
  