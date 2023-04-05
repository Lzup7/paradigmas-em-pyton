try:

  def verificar_impar_par():
      if (resultado_operacao // 1 == resultado_operacao):
          print("Inteiro")
          if resultado_operacao % 2 == 0:
              print("Par")
              if resultado_operacao > 0:
                  print("Positivo")
              else:
                  print("Negativo")
          else:
              print("Impar")
      else:
          print("Decimal")
  
  numero1 = float(input("Digite o número 1: "))
  numero2 = float(input("Digite o número 2: "))
  operacao = input("Digite a operação desejada: +, -, /, * : ")
  operadores = "+ - / *"
  
  if operacao in operadores:
    if operacao == "+":
        
        resultado_operacao = numero1 + numero2
        print(f"Resultado: {resultado_operacao}")  
        verificar_impar_par()
    elif operacao == "-":
        resultado_operacao = numero1 - numero2
        print(f"Resultado: {resultado_operacao}") 
        verificar_impar_par()
    elif operacao == "/":
        resultado_operacao = numero1 / numero2
        print(f"Resultado: {resultado_operacao}") 
        verificar_impar_par()
    elif operacao == "*":
        resultado_operacao = numero1 * numero2
        print(f"Resultado: {resultado_operacao}")
        verificar_impar_par()
    else:
        print("Erro\nSelecione um valor valido")
  else: 
    print("Erro\nSelecione um valor valido")
except:
  print("Erro\nSelecione um valor valido")
