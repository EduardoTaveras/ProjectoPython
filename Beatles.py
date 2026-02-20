banda = []
print(f"\nPaso 1: {banda}")

banda.append("John Lennon")
banda.append("Paul McCartney")
banda.append("George Harrison")
print(f"\nPaso 2: {banda}")

for miembros in range(2):
    banda.append(input("Nuevos miembros de la banda: "))
print(f"\nPaso 3: {banda}")

del banda[-1]
del banda[-1]
print(f"\nPaso 4: {banda}")

banda.insert(0, "Ringo Starr")
print(f"\nPaso 5: El grupo finalmente es: {banda}")

print(f"\nPaso 6: La cantidad de miembros es:  {len(banda)}")

print(f"\nPaso 7: Este es un cambio para la tarea de las ramas")