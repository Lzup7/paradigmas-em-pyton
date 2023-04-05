
while True:
  try:
    valor_hora = float(input("Quanto você ganha por hora: R$"))
    horas = float(input("Quantas horas você trabalha por mes: "))
    salario_bruto = valor_hora * horas
    print(f"\nSalario Bruto:R${salario_bruto:.2f}")
    if 0 < salario_bruto:
      if 0 < salario_bruto <= 900 :
        sindicato = 0.03 * salario_bruto
        fgts = 0.11 * salario_bruto
        salario_liquido = salario_bruto - sindicato
        print(f"Sindicato: R${sindicato:.2f}\nFgts: R${fgts:.2f}\nTotal desconto: R${sindicato:.2f}\nSalario Liquido: R${salario_liquido:.2f}")
        break
      elif 900 < salario_bruto <= 1500 :
        sindicato = 0.03 * salario_bruto
        fgts = 0.11 * salario_bruto
        imposto_renda = 0.05 * salario_bruto
        total_desconto = sindicato + imposto_renda
        salario_liquido = salario_bruto - (total_desconto)
        print(f"Sindicato: R${sindicato:.2f}\nFgts: R${fgts:.2f}\nImposto de renda: R${imposto_renda:.2f}\nTotal desconto: R${total_desconto:.2f}\nSalario Liquido: R${salario_liquido:.2f}")
        break
      elif 1500 < salario_bruto <= 2500 :
        sindicato = 0.03 * salario_bruto
        fgts = 0.11 * salario_bruto
        imposto_renda = 0.10 * salario_bruto
        total_desconto = sindicato + imposto_renda
        salario_liquido = salario_bruto - (total_desconto)
        print(f"Sindicato: R${sindicato:.2f}\nFgts: R${fgts:.2f}\nImposto de renda: R${imposto_renda:.2f}\nTotal desconto: R${total_desconto:.2f}\nSalario Liquido: R${salario_liquido:.2f}")
        break
      elif 2500 < salario_bruto :
       sindicato = 0.03 * salario_bruto
       fgts = 0.11 * salario_bruto
       imposto_renda = 0.20 * salario_bruto
       total_desconto = sindicato + imposto_renda
       salario_liquido = salario_bruto - (total_desconto)
       print(f"Sindicato: R${sindicato:.2f}\nFgts: R${fgts:.2f}\nImposto de renda: R${imposto_renda:.2f}\nTotal desconto: R${total_desconto:.2f}\nSalario Liquido: R${salario_liquido:.2f}")
      break
    else:
      print("\nErro\nSelecione um valor valido:\n")
      
      
  except:
    print("\nErro\nSelecione um valor valido:\n")