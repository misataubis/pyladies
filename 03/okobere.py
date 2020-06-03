from random import randrange
pStav = 0
pKarta = 0
pKonec = 'ne'
while pKonec == 'ne' and pStav < 21:
	pKarta = 2 + randrange (9)
	pStav = pStav + pKarta
	print('Karta: ', pKarta, '  Nový stav: ', pStav)
	if pStav < 21: pKonec = input ('Skončit?')
if pStav > 21:
	print('Looser')
else:
	print('Winner!')
	
	

