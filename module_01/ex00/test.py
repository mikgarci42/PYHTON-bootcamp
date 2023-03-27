def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento

ciudad_devueltas = devuelve_ciudades(["Madrid", "Alicante"], "Barcelona")

print(next(ciudad_devueltas))