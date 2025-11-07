# Programa per calcular operacions bàsiques amb dos nombres enters

# Demanem els nombres a l'usuari
num1 = int(input("Introdueix el primer nombre enter: "))
num2 = int(input("Introdueix el segon nombre enter: "))

# Calculem les operacions
suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2

# Evitem divisió per zero
if num2 != 0:
    divisio = num1 / num2
else:
    divisio = "No es pot dividir entre zero"

# Mostrem els resultats
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicació: {multiplicacio}")
print
