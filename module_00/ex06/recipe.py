#!/usr/bin/python3

def print_recetas(book):
    print("Las recetas que hay son las sigueintes:", end=" ")
    for x in list(book)[0:len(book) - 1]: print(x, end=", ")
    print(list(book.keys())[-1])

def print_unareceta(receta):
    for i in dcbook:
        if i == receta:
            interno = dcbook[i]
            for x, y in interno.items(): print(x, y)
            return 
    print("No se ha encontrado la receta")
    
def delete_item(receta):
    for i in dcbook:
        if i == receta:
            dcbook.pop(i)
            return
    print("No se ha encontrado la receta")


d1 = {
    "ingedientes": ["jamon", "pan", "queso", "tomate"], 
    "meal": "almuerzo",
    "prep_time": 10
}

d2 = {
    "ingedientes": ["harina", "azucar", "huevos"], 
    "meal": "almuerzo",
    "prep_time": 60
}

d3 = {
    "ingedientes": ["aguacate", "rucula", "tomates", "espinacas"], 
    "meal": "almuerzo",
    "prep_time": 15
}

dcbook = {
    "bocadillo": d1,
    "tarta": d2,
    "ensalada": d3
}

if __name__ == "__main__":
    print_recetas(dcbook)
    print_unareceta("caca")
    delete_item("tarta")
    print_recetas(dcbook)

