#lista = list((1,2,3)) # deklaracja listy
lista = [1,2,3] # inna delkaracja tej samej listy

print(lista)
print(lista[0]) #dobranie sie do pierwszego elementu
print(lista[-1]) #dobranie sie do ostatniego elementu
print(type(lista[0])) # typ elementu
print(type("ciag znakow"))
print(type(1.2))
print(type(b'b')) # standard ASCII
print(type(lista))
print([1, ['druga lista']]) # listy moga przechowywac inne list, a listy moga przechowac zmienne roznych typo
print([[1,2,3], [4,5,6]])
macierz = [[0]*10]*10 # tablica 10x10, zwodnicza! jest elementy tablicy (rzędy) to odnośniki do tej samej listy dziesięcioelementowej wypełnionej zerami
print(macierz)
macierz = [0]*10
# for row in macierz:
#     row = [0]*10
print(len(macierz)) # zwraca długość iterowalnej zmiennej
for index in range(len(macierz)): # nie można iterować po nieiterowalnych
    print(index)
    macierz[index] = [0] * 10

macierz[4][4] = 5
for row in macierz:
    print(row)

# range dwuargumentowy
for liczba in range(5, 7):
    print(liczba)

if 5 < 7: # warunek
    print('prawda') # jezeli prawdziwy
else:
    print('fałsz') # jezeli falszywy