negatiu = False
for i in range(10):
    nombre = float(input("Introdueix el nombre: "))
    if nombre < 0:
        negatiu = True
        break

if negatiu:
    print("hi havia almenys un nombre negatiu")
else:
    print("no hi ha cap nombre negatiu")

# Programa que demana 10 nombres a l'usuari i comprova si hi ha algun nombre negatiu.
# Ho he fet amb un bucle for i una variable.
# Si poses almenys un nombre negatiu, el programa t'ho diu.