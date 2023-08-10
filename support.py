from csv import reader

def import_csv_layout(path):
    with open(path) as map: 
        level = reader(map,delimeter = ',')
        
        for row in level:
            print(row)