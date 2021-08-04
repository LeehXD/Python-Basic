algo = input('Digite algo:')
print('O tipo primitivo é', type(algo))
print('Isso possui letras e numeros?{}'.format(algo.isalnum()))  #isalnum o conteudo é um numero ou letra
print('Isso é um numero?{}'.format(algo.isnumeric()))  #isnumeric o conteudo é um numero
print('Isso é uma letra?{}'.format(algo.isalpha()))  #isalpha o conteudo possui apenas letras
print('Isso está em maiusculo?{}'.format(algo.isupper()))  #isupper o conteudo é em maiusculo
print('Isso está em minusculo?{}'.format(algo.islower()))  #islower o conteudo está em minusculo
print('Está capitalizada?{}'.format(algo.istitle())) #não está nem maiusculas nem minusculas
print('Só tem espaço?{}'.format(algo.isspace())) # isspace informa que á apenas espaço



#COMENTARIO