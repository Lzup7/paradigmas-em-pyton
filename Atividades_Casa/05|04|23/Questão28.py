while True:
  try:
    tipo_carne = int(input("Qual tipo da carne que irá comprar:\n1(file duplo)\n2(alcatra)\n3(picanha)\n: "))
    if 0 < tipo_carne < 4 :
      quantidade_carne = int(input("Digite a quantidade de carne que irá comprar: "))
      tipo_pagamento = input("Escreva o tipo de tipo de pagamento:\nCartão Tabajara(C)\nOutro(O)\n: ").upper()
      if tipo_pagamento in "CO" :
      
        print(f"Tipo de carne: {tipo_carne} \nQuantidade de carne: {quantidade_carne}")
        
        preco_file_duplo1 = quantidade_carne * 4.90
        preco_file_duplo2 = quantidade_carne * 5.80
        
        alcatra1 = quantidade_carne * 5.90
        alcatra2 = quantidade_carne * 6.80
        
        picanha1 = quantidade_carne * 6.90
        picanha2 = quantidade_carne * 7.80
        
        if tipo_carne == 1:
            if quantidade_carne > 5:
                preco_total = preco_file_duplo1
            else:
                preco_total = preco_file_duplo2
        elif tipo_carne == 2 :
            if quantidade_carne > 5:
                preco_total = alcatra1
            else:
                preco_total = alcatra2
        elif tipo_carne == 3:
            if quantidade_carne > 5:
                preco_total = picanha1
            else:
                preco_total = picanha2
        else:
            print("Carne Invalida")
        
        if tipo_pagamento == "C":
            desconto = preco_total * 0.05
            print(f"Tipo de pagamento: Cartão Tabajara")
            print(f"Valor do desconto: {desconto:.2f}")
            print(f"Valor Final: {(preco_total - desconto):.2f}")
        else:
            print("Tipo de pagamento: Outro\nValor do desconto: 0")
            print(f"Valor Final: {preco_total:.2f} ")
        break
      else:
       print("\nErro\nSelecione um valor valido:\n") 
    else:
      print("\nErro\nSelecione um valor valido:\n")
  except:
     print("\nErro\nSelecione um valor valido:\n")