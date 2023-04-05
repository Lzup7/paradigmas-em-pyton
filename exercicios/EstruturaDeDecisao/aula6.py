
print("Digite tres numeros de 0 a 10")

numero1 = int(input("Qual o primeiro numero: "))
numero2 = int(input("Qual o segundo numero: "))
numero3 = int(input("Qual o terceiro numero: "))

if (numero1 <= 10 and numero1 > 0) and (numero2 <= 10 and numero2 > 0) and (numero3 <= 10 and numero3 > 0):

  if numero1 > numero2 and numero1 > numero3 :
    print(f"O numero {numero1} é o maior numero ")
  
  elif numero2 > numero1 and numero2 > numero3 :
    print(f"O numero {numero2} é o maior numero ")
  
  elif numero3 > numero1 and numero3 > numero2 :
    print(f"O numero {numero3} é o maior numero ")

else:
  print ("\n !Atenção!\nAcione um numero valido!")