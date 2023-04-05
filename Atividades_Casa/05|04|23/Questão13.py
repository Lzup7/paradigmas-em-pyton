while True:
 try:
   dia_semana = int(input("Dia da semana: "))
   if 1 <= dia_semana <= 6 :
     if dia_semana == 1:
       print("Domingo")
       break
     elif dia_semana == 2:
       print("Segunda")
       break
     elif dia_semana == 3:
       print("Terça")
       break
     elif dia_semana == 4:
       print("Quarta")
       break
     elif dia_semana == 5:
       print("Quinta")
       break
     elif dia_semana == 6:
       print("Sexta")
       break
   else:
     print("\nDigite um numero valido!\nDe 1 a 6.\n")
 except:
   print("\nErro:\nSelecione um valor valido:\n")