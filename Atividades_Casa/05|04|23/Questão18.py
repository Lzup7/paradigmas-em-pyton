dia = int(input("Selecione o dia: "))
if 0 < dia < 32 :
  Mes = int(input("Selecione o Mes: "))
  if 0 < Mes < 13 :
   ano = int(input("Selecione o ano: "))
   if 0< ano :
      print(f"A data é {dia}|{Mes}|{ano}")

   else:
      print("Selecione um ano valido")
     
  else:
   print("Selecione um Mes valido")
     
else:
  print("Selecione um dia valido")
 