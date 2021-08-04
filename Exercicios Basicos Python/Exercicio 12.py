valor = float(input('Qual o preço do produto R$'))
calculo = valor * 5 / 100
resultado = valor - calculo
print('Desconto é de 5%\n'
         'Valor do desconto R${:.2f}\n'
         'Preço com desconto R${:.2f}' .format(calculo, resultado))
