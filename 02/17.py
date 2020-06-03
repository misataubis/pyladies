from random import randrange
cislo = randrange (3)
if cislo == 0: tah_pocitace = 'kámen'
elif cislo == 1: tah_pocitace = 'nůžky'
else: tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír? ')
print ('počítač táhl: ',tah_pocitace)
if tah_cloveka == tah_pocitace:
        print(tah_pocitace,'=', tah_cloveka, 'plichta.')
elif ((tah_pocitace == 'nůžky') and (tah_cloveka == 'kámen')) or ((tah_pocitace == 'kámen') and (tah_cloveka == 'papír')) or ((tah_pocitace == 'papír') and (tah_cloveka == 'nůžky')):
        print(tah_pocitace,'<', tah_cloveka, 'vyhrála jsi!')
elif ((tah_pocitace == 'kámen') and (tah_cloveka == 'nůžky')) or ((tah_pocitace == 'papír') and (tah_cloveka == 'kámen')) or ((tah_pocitace == 'nůžky') and (tah_cloveka == 'papír')):
        print(tah_pocitace,'>', tah_cloveka, 'počítač vyhrál')
else:
    print('nerozumím.')