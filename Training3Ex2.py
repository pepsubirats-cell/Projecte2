# Programa que demana tres nombres i mostra quin és el més gran
a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
c = int(input("Introdueix el tercer nombre: "))

#Comprovem quin és el més gran
if a >= b and a >= c:
    print(f"El nombre més gran és: {a}")
elif b >= a and b >= c:
    print(f"El nombre més gran és: {b}")        
else:
    print(f"El nombre més gran és: {c}")