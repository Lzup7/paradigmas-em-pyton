morangos = int(input("Digite a quantidade de morangos em kg: "))
macas = int(input("Digite a quantidade de maças em kg: "))
preco_morango1 = morangos * 2.50
preco_morango2 = morangos * 2.20

preco_maca1 = macas * 1.80
preco_maca2 = macas * 1.50

print(f"quantidade de maçãs: {macas}\nQuantidade de morangos: {morangos} ")

if morangos > 5:
    preco_morango = preco_morango1
else:
    preco_morango = preco_morango2

if macas > 5:
    preco_maca = preco_maca1
else:
    preco_maca = preco_maca2

preco_total = preco_maca + preco_morango

if preco_total > 25 or (macas + morangos) > 8:
    print(f"Preço final: {(preco_total - (preco_total * 0.1)):.2f}")
else:
    print(f"Preço final: {preco_total:.2f}")