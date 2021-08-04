dias = int(input('Quantos dias foi alugado?'))
km = float(input('Quantos Km rodados?'))
result = (dias * 60) + (km * 0.15)
print('Total a pagar R${:.2f}'.format(result))
