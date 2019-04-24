def print_macierz(macierz):
    for row in macierz:
        print(row)

# sprawdza ilosc sasiadow komorki i zwraca ich liczbe
def neighbours(macierz, row, column):
    number_of_rows = len(macierz) -1 # zwaraca długość, czyli długość o jeden większą od maksymalnego indexu
    number_of_cols = len(macierz[0]) -1  # działa pod warunkiem że pracujemy na strukturze o prostokatnym kształcie
    # TODO: Uogólnic dla wszystkich przypadków
    sasiedzi = 0
    if macierz[row][column] == 1:
        sasiedzi = -1
    # TODO: Inne rozwiązanie wykorzystujace zawijanie się planszy tzn. łączące przeciwległe krawędzie
    for r in range(max(row-1, 0), min(row+2, number_of_rows)):
        for c in range(max(column-1,0), min(column+2, number_of_cols)):
            if macierz[r][c] == 1: # ==, oraz is - nie są tożsame
                # tutaj jeżeli prawda
                #sasiedzi = sasiedzi + 1 # rownowazne z linia nizej
                sasiedzi += 1
    return sasiedzi

def macierz_zerowa(rows, colums):
    macierz = [0] * rows
    for index in range(len(macierz)):  # nie można iterować po nieiterowalnych
        macierz[index] = [0] * colums
    return macierz

def cycle_of_life(macierz, macierz_pomocnicza):
    for row_index in range(len(macierz)):
        for col_index in range(len(macierz[row_index])):
            liczba_sasiadow = macierz_pomocnicza[row_index][col_index]
            if macierz[row_index][col_index] == 1: # żywa
                if liczba_sasiadow < 2: # smierc z braku sasiadow
                    next_state = 0
                elif liczba_sasiadow > 3: # smierc z przeludnienia
                    next_state = 0
                else: # liczba sąsiadów od 2 do 3, wieć komórka zostaje żywa
                    next_state = 1
            elif macierz[row_index][col_index] == 0 and liczba_sasiadow == 3: #martwa, 3 sasiadów ożywa
               next_state = 1
            else:
                next_state = 0
            macierz[row_index][col_index] = next_state
    return macierz

# Tworzenie macierzy 10x10 prawidlowo dzialajacej
macierz_pomocnicza = macierz_zerowa(10,10)
macierz = macierz_zerowa(10,10)


macierz[1][2] = 1 #[2,3]
macierz[1][3] = 1 #[2,4]
macierz[1][4] = 1 #[2,5]
#macierz[3][2] = 1 #[4,3]
print_macierz(macierz)
var = neighbours(macierz, 1,2)
print(var) # powinno byc 1
print(neighbours(macierz, 3,2)) # powinno byc 0

# Liczenie macierzy sąsiadów
import time
import os
while True:
    for row_index in range(len(macierz)):
        for col_index in range(len(macierz[row_index])):
            macierz_pomocnicza[row_index][col_index] = neighbours(macierz, row_index, col_index)

    #print_macierz(macierz_pomocnicza)
    macierz = cycle_of_life(macierz, macierz_pomocnicza)
    print_macierz(macierz)
    print("")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
#print_macierz(macierz)