# creazione di una calcolatrice in python

from math import sqrt

# con tre virgolette la stringa ha più righe
hello_message = """
Benvenuti al programma calcolatrice.

Di seguito un elenco delle varie funzioni disponibili:

- Per effettuare un'Addizione, selezionare 1;
- Per effettuare una Sottrazione, selezionare 2;
- Per effettuare una Moltiplicazione, selezionare 3;
- Per effettuare una Divisione, selezionare 4;
- Per effettuare un Calcolo Esponenziale, selezionare 5;
- Per effettuare una Radice Quadrata, selezionare 6;
- Per uscire dal programma, digitare ESC
"""

while True:
  print(hello_message)
  
  action = input("Inserisci il numero corrispondente all'operazione da effettuare: ")
  
  if action == "1":
    print("\nHai scelto Addizione\n")
    a = float(input("Inserici il primo numero -> "))
    b = float(input("Inserici il secondo numero -> "))
    print("Il risultato dell'Addizione è: ", str(a + b))
  
  elif action == "2":
    print("\nHai scelto Sottrazione\n")
    a = float(input("Inserici il primo numero -> "))
    b = float(input("Inserici il secondo numero -> "))
    print("Il risultato della Sottrazione è: ", str(a - b))
  elif action == "3":
    print("\nHai scelto Moltiplicazione\n")
    a = float(input("Inserici il primo numero -> "))
    b = float(input("Inserici il secondo numero -> "))
    print("Il risultato della Moltiplicazoine è: ", str(a * b))
  elif action == "4":
    print("\nHai scelto Divisione\n")
    a = float(input("Inserici il primo numero -> "))
    b = float(input("Inserici il secondo numero -> "))
    print("Il risultato della Divisione è: ", str(a / b))
  elif action == "5":
    print("\nHai scelto Calcolo Esponenziale\n")
    a = float(input("Inserici la base -> "))
    b = float(input("Inserici l'esponente -> "))
    print("Il risultato del Calcolo Esponenziale è: ", str(a ** b))
  elif action == "6":
    print("\nHai scelto Radice Quadrata\n")
    a = float(input("Inserici il numero -> "))
    print("Il risultato dell'operazione è: ", str(sqrt(a)))
  elif action == "Esc":
    print("\nL'applicazione verrà chiusa\n")
    break
  
  new_action = input("Vuoi continuare ad utilizzare l'applicazione? S/N ")
  if new_action == "N" or new_action == "n":
    print("A presto\n")
    break
  
  print("sto tornando al menù principale\n")