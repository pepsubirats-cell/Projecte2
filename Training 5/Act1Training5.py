from time import sleep

def ex1_area():
    costat = float(input("Introdueix la mida del costat del quadrat: "))
    area = costat ** 2
    print(f"L'àrea del quadrat és: {area}")

def ex2_operacions():
    num1 = int(input("Introdueix el primer nombre enter: "))
    num2 = int(input("Introdueix el segon nombre enter: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacio = num1 * num2


    if num2 != 0:
        divisio = num1 / num2
    else:
     divisio = "No es pot dividir entre zero"
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicació: {multiplicacio}")
    print (f"Divisió: {divisio}")

def ex3_frase():
    paraula1 = input("Introdueix la primera paraula: ")
    paraula2 = input("Introdueix la segona paraula: ")
    paraula3 = input("Introdueix la tercera paraula: ")

    frase = f"{paraula1} {paraula2} {paraula3}"

    print("La frase creada és:", frase)

def ex4_enters():
    num1 = float(input("Introdueix el primer nombre amb decimals: "))
    num2 = float(input("Introdueix el segon nombre amb decimals: "))


    num1_enter = int(num1)
    num2_enter = int(num2)


    print(f"El primer nombre convertit a enter és: {num1_enter}")
    print(f"El segon nombre convertit a enter és: {num2_enter}")

def ex5_edat():
    edat = input("Quina és la teva edat?: ")
    if edat.isdigit():
        edat = int(edat)
        if edat < 18:
            print("Ets menor d'edat.")
        else:
            print("Ets major d'edat.")
    else:
        print("Si us plau, introdueix un nombre vàlid.")

def ex6_gran():
    

    a = int(input("Introdueix el primer nombre: "))
    b = int(input("Introdueix el segon nombre: "))
    c = int(input("Introdueix el tercer nombre: "))

    if a >= b and a >= c:
        print(f"El nombre més gran és: {a}")
    elif b >= a and b >= c:
        print(f"El nombre més gran és: {b}")        
    else:
        print(f"El nombre més gran és: {c}")
    
def ex7_positiu():
    num = int(input("Introdueix un nombre: "))
    if num >= 0:
        print("El nombre és positiu.")
    else:
        print("El nombre és negatiu.")

def ex8_parells():
    for num in range(2, 201, 2):
        print(num)

def ex9_nota():
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

def ex10_negatius():
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



if __name__ == "__main__":
    while True:
        print("\n--- MENÚ ---")
        print("1. Àrea")
        print("2. Operacions")
        print("3. Frase")
        print("4. Enters")
        print("5. Edat")
        print("6. Més gran")
        print("7. Positiu/Negatiu")
        print("8. Parells")
        print("9. Nota 10")
        print("10. Negatius")
        print("S. Sortir")
        
        op = input("Tria una opció del 1 al 10: ")

        op = op.upper()
        
        match op:
            case "1":
                ex1_area()
            case "2":
                ex2_operacions()
            case "3":
                ex3_frase()
            case "4":
                ex4_enters()
            case "5":
                ex5_edat()
            case "6":
                ex6_gran()
            case "7":
                ex7_positiu()
            case "8":
                ex8_parells()
            case "9":
                ex9_nota()
            case "10":
                ex10_negatius()
            case "S":
                print("Sortint...")
                break
            case _:
                print("Opció no vàlida.")
        sleep(2)

