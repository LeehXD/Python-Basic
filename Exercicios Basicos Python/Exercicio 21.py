from math import radians, sin, cos, tan #especificando qual termo será usado não é precisp repetir no carpo do programa (math)
angulo = float(input('Digite o angulo que você deseja:'))
seno = sin(radians(angulo)) # o termo sen faz o calculo do seno de um angulo
coseno = cos(radians(angulo)) # o termo cos faz o calculo do coseno de um angulo
tangente = tan(radians(angulo))  # o termo tan faz o calculo da tangente de um angulo

print('Angulo: {:.0f}º'
      '\nSeno: {:.2f}'
      '\nCoseno: {:.2f}'
      '\nTangente: {:.2f}'
      .format(angulo, seno, coseno, tangente))