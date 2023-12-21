# napisi aplikaciju koja ce od korisnka traziti unos ime i prezimena osobe.
# neka se unos ponavalja sve dok god korisnik to zeli.
rjecnik = {}
indeks = 1

while True:
    ime = input('Unesite ime: ')
    prezime = input('Unesite prezime: ')

    rjecnik[indeks] = [ime, prezime]
    indeks += 1

    upit = input('Zelite li unijeti novu osobu? (Da/Ne): ')
    if upit.lower() == 'ne':
        break


for key, value in rjecnik.items():
    print(key, end=' ')
    for item in value:
        print(item, end=' ')
    
    print()


print('\n')
