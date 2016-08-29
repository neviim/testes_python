#neste determina aqui mesmo
r_arq = open('./veni.txt', 'r')

for linha in r_arq.readlines():
  print linha
  
r_arq.close()
