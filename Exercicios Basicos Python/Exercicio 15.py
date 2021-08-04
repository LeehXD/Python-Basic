metros = float(input('Digite um valor em metros:'))
dm = metros * 10
cm = metros * 100
mm = metros * 1000
m = metros
dam = metros / 10
hec = metros / 100
km = metros / 1000
print('O valor {} metros, corresponde a:\n'
      'Decimetro={}\n'
      'Centimetro={}\n'
      'Milimetro={}\n'
      'Decametro={}\n'
      'Hectometro={}\n'
      'Quilometro={}\n'
      .format(metros, dm, cm, mm, dam, hec, km))