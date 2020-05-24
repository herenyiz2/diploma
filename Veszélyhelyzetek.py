
#a program először betölti a csv fájl tartalmát, majd kiírja az összes elemét, amiket amugy egy listába olvas. 
# majd hozzáír a csv hez még egy sort, és a meggyőződés céljából mégegyszer kiolvasom a fájl tartalmát, és ujra kiírom.

from csv import reader
 
# csv fájlból beolvasás
with open('Veszélyhelyzetek.csv', 'r') as read_obj:
    # A fájl átadása az olvasó objektumnak
    csv_reader = reader(read_obj)
    # A kiolvasott eredmény átadása egy listát készítő metődusnak, hogy az eredményünk egy listába legyen végül
    list_of_rows = list(csv_reader)
    print(list_of_rows)



# A csv fájlból kiválasztjuk a 3 sor 2 oszlop elemét
row_number = 3
col_number = 2
value = list_of_rows[row_number - 1][col_number - 1]
 
print('A 3 sor 2 oszlop eleme : ', value)



from csv import writer

def append_list_as_row(file_name, list_of_elem):
    # Fájl megnyitása hozzáfűzésre
    with open(file_name, 'a+', newline='') as write_obj:
        # writer objektum létrehozása a csv fájlhoz
        csv_writer = writer(write_obj)
        # Elemek hozzáadása a csv fájlhoz
        csv_writer.writerow(list_of_elem)

# A lista a hiányzó elemekkel (ezek lesznek hozzáadva a listához)
row_contents = []
 
# A hiányzó elemek a csv fájlhoz való hozzáadása
append_list_as_row('Veszélyhelyzetek.csv', row_contents)

# egy üres sor írása, hogy ne legyen egybe ömlesztve az output
print()
# Mivel hozzáadtam az új elemeket, újra kiiratom ,hogy meglássam tényleg ott vannak e az új elemek
with open('Veszélyhelyzetek.csv', 'r') as read_obj:
    # A fájl átadása az olvasó objektumnak
    csv_reader = reader(read_obj)
    # A kiolvasott eredmény átadása egy listát készítő metődusnak, hogy az eredményünk egy listába legyen végül
    list_of_rows = list(csv_reader)
    print(list_of_rows)
