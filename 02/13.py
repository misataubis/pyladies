výška = float (input('Kolik měříš v metrech? '))
if výška >= 1.9:
    print('Ty jsi ale obr! Neuvažuješ o hraní NBA?')
elif ((výška >= 1.5) and (výška < 1.9)):
    print('Průměrný člověk, nuda.')
elif ((výška >= 0.4) and (výška < 1.5)):
    print('Dítě nebo liliput?')
elif ((výška > 0) and (výška < 0.4)):
    print('JSi si jistý, že jsi pořád ještě člověk?')
else:
    print('Nekladné hodnoty nepřipadají v úvahu.')