litros = int(input("Digite a quantidade de litros: "))
combustivel = input("Digite o tipo do combustivel G/A: ").upper()

preco_alcool1 = (1.90 * 0.03)
preco_alcool2 = (1.90 * 0.05)
preco_gasolina1 = (2.50 * 0.04)
preco_gasolina2 = (2.50 * 0.06)

print(f"Litros Vendidos: {litros} ")

if combustivel == "A":
    print("Combustivel: alcool")
    if litros <= 20:
        desconto = (1.90 - preco_alcool1) * litros
        print(f"Preço: {desconto:.2f} ")
    else:
        desconto = (1.90 - preco_alcool2) * litros
        print(f"Preço: {desconto:.2f} ")
elif combustivel == "G":
    print("Combustivel: gasolina")
    if litros <= 20:
        desconto = (2.50 - preco_gasolina1) * litros
        print(f"Preço: {desconto:.2f} ")
    else:
        desconto = (2.50 - preco_gasolina2) * litros
        print(f"Preço: {desconto:.2f} ")
else:
    print("Erro\nValor Invalido")