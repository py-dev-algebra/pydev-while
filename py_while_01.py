brojevi = []
for broj in range(1, 51):
    brojevi.append(broj)


for broj in brojevi:
    print(broj, end=' ')
print('\n')


brojac = 0
while brojac < len(brojevi):
    print(brojevi[brojac], end=' ')
    brojac += 1


print('\n')