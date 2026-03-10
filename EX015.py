D = int(input('Quantos dias alugados:'))
Km = float (input('Quantos km o carro rodou:'))
Total = (D * 60) + (Km * 0.15)

print(f'Joao gastou {D} dias na viagem e percorreu {Km}Km, o valor pago pelo aluguel do carro foi de:{Total}')