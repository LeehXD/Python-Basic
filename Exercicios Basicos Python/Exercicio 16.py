graus = float(input('Informe a temperatura em graus Celsius '))
conversaoF = graus * (9/5) + 32
conversaoK = graus + 273.15
print(' Conversão\n'
      'Graus Celsius: {}ºC\n'
      'Fahrenheit: {}ºF \n'
      'kelvin: {}ºK'
      .format(graus, conversaoF, conversaoK))
