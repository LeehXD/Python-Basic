''''
ca = float(input('Informe o cateto adjacente:'))
co = float(input('Informe o cateto oposto:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa mede: {:.2f}'
.format(hi))
'''
#conta sem função match

'''
import math
co = float(input('Informe o cateto oposto:'))
ca = float(input('Informe o cateto adjacente:'))
print('A hipotenusa deste triângulo retângulo é: {:.2f}'
      .format(math.hypot(co, ca)))
      '''
#hypot é utilizado para fazer o calculo da hipotenusa