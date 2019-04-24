literki = ['a', 'b', 'c', 'd']

for literka in literki: # nielegalne jest przypisywanie wartości, które mają zostać zachowane
    print(literka)

for i in range(len(literki)):
    print(i)
    print((literki[i]))

for i, literka in enumerate(literki):
    print(i, literka)