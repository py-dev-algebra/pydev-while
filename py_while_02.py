titula = 'Pythggon Programer(ka)'

# for slovo in 'Python Programer(ka)':
for slovo in titula:
    if slovo == 'g':
        # break # - prekida izvrsavanje petlje i izlazi iz petlje
        # continue
        pass # nekakav kod koji ce izvrsiti nekakve obrade

    print(slovo, end=' ')

print('\n')
print('Nakon break')
print('\n')
print('\n')


while True:
    # Izbornik
    print(40 * '*')
    print('\tAlgebra PyDev')
    print('\tNaziv aplikacije')
    print(40 * '*')
    print()
    print('1. Unos novog zapisa')
    print('2. Editiranje zapisa')
    print('0. Izlaz')
    print()

    izbor_korisnika = int(input('Izaberite jedan broj iz izbornika: '))
    print()

    if izbor_korisnika == 1:
        print('Pokrenuta funkcija unosa novog zapisa')
    elif izbor_korisnika == 2:
        print('Pokrenuta funkcija editiranja zapisa')
    elif izbor_korisnika == 0:
        print('Pokrenuta funkcija izlaza iz aplikacije')
        break

    print()

    upit = input('Zelite li ponoviti akciju? (Da/Ne): ')
    if upit.lower() == 'ne':
        break


print('\n')