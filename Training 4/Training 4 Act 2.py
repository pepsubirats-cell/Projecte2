notes = [5, 6, 7, 8, 9]

while True:
    nota = int(input("Introdueix una nota (o -1 per acabar): "))
    if nota == -1:
        break
    notes.append(nota)

if 10 in notes:
    print("Hi ha hagut alguna nota amb un 10.")
else:
    print("No hi ha cap 10.")

# Programa que demana notes a l'usuari fins que introdueix -1.
# Després comprova si hi ha hagut alguna nota amb un 10.
# Ho he fet amb un bucle while i una llista.