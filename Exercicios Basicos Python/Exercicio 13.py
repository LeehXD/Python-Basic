nome = input('Digite seu nome:')
salario = float(input('Digite seu salário R$'))
resultado = salario + (salario * 15 / 100)
print('Sr(a){}\n'
      'Parabéns ouve um aumento de 15% em seu salário.\n'
      'Salário atualizado R${}'
      .format(nome,resultado))

