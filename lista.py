#Este pequeño programa crea una lista y realiza varias modificaciones.

lista = [1, 2.0, "tres", 4, 5.0, "seis"]

print(f"\nLista original {lista}")

lista[0] = "uno"

print(f"\nLista actualizada {lista}")

lista[4] = lista[1]

print(f"\nLista con cambios {lista}")

print(f"\nLogitud de la lista: {len(lista)}")