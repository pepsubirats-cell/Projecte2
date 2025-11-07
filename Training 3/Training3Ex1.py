# Programa que demana l'edat i diu si ets major o menor d'edat

# Demanem a l'usuari que introdueixi la seva edat
edat = input("Quina és la teva edat?: ")
if edat.isdigit():
    edat = int(edat)
  # Comprovem si l'edat és igual o superior a 18
    if edat < 18:
        print("Ets menor d'edat.")
 # Si no, vol dir que és menor de 1
    else    :
        print("Ets major d'edat.")
