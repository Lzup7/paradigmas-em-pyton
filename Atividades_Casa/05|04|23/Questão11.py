while True:
  try:
    salario = float(input("Digite seu salario: R$"))
    if 0 < salario <= 280 :
      reajuste = salario * 0.20
      salario_reajustado = salario + reajuste
      print(f"O seu salario era R${salario:.2f}.\nSofreu em reajuste de 20%. isso é R${reajuste:.2f}.\nSeu novo salario reajustado é R${salario_reajustado:.2f}")
      break
    elif 280 < salario <= 700 :
      reajuste = salario * 0.15
      salario_reajustado = salario + reajuste
      print(f"O seu salario era R${salario:.2f}.\nSofreu em reajuste de 15%. isso é R${reajuste:.2f}.\nSeu novo salario reajustado é R${salario_reajustado:.2f}")
      break
    elif 700 < salario <= 1500 :
      reajuste = salario * 0.10
      salario_reajustado = salario + reajuste
      print(f"O seu salario era R${salario:.2f}.\nSofreu em reajuste de 10%. isso é R${reajuste:.2f}.\nSeu novo salario reajustado é R${salario_reajustado:.2f}")
      break
    elif 1500 < salario  :
      reajuste = salario * 0.05
      salario_reajustado = salario + reajuste
      print(f"O seu salario era R${salario:.2f}.\nSofreu em reajuste de 5%. isso é R${reajuste:.2f}.\nSeu novo salario reajustado é R${salario_reajustado:.2f}")
      break
    else:
     print("\nErro:\ndigite um valor valido!\n")    
  except:
    print("\nErro:\ndigite um valor valido!\n")