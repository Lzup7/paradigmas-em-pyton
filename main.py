try:
  operação = int(input("Selecione o tipo da operação:\n(1)Adição\n(2)Subtração\n(3)Multiplicação\n(4)Divisão\n: "))
  if 0 < operação < 5 :
    try:
      numero1 = int(input("Selecione o primeiro numero: "))
      numero2 = int(input("Selecione o Segundo numero: "))

      match operação:
       case 1:
        result1 = numero1 + numero2
        print(f"A soma de {numero1} e {numero2} é {result1}\nResultado {result1} ")     
       case 2 :
        result2 = numero1 - numero2
        print(f"A subtração de {numero1} e {numero2} é {result2}\nResultado {result2} ")
       case 3 :
        if not numero1 == 0 or numero2 == 0 :
          result3 = numero1 * numero2
          print(f"A Multiplicação de {numero1} e {numero2} é {result3}\nResultado {result3} ")
       case 4:
           print(f"A Multiplicação de {numero1} e {numero2} é 0\nResultado 0 ")
     
    except:
      print("Erro\nDigite um numero valido")
  else:
    print("Erro:\nSelecione uma operação valida de 1 a 4.")    
except ValueError:
  print("\nErro:\nSelecione um numero valido.")

  