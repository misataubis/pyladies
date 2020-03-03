# Původní zadání: print('Obvod čtverce se stranou 356 cm je', 4 * 356, 'cm')
# Původní zadání: print('Obsah čtverce se stranou 356 cm je', 356 * 356, 'cm')

# Proměnná a převod na číslo
strana = int(input('Zadej délku strany čtverce v cm'))
print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')

#Porovnání pomocí operátorů
strana = int(input('Zadej délku strany čtverce v cm'))
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
else:
    print('Hodnota musí být kladná')

print('Děkujeme za použití naší geometrické kalkulačky')

