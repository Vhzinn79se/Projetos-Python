tenis = float(input('digite o valor do tenis: '))

desconto = tenis * 5/100
novo_preco = tenis - desconto

print(f'O valor do tenis é de:{tenis:.2f} e somente hoje com 5% de desconto esta saindo de: {novo_preco:.2f}' )