max_materie = 3
materie=int(input("Inserisci numero di materie: "))

if materie > max_materie:
	print("superato numero massimo di materie possibili")
	exit()

file = open("MATERIE.csv", "w+")
file.write("IdMateria, Materia")

materia=dict()

for a in range(materie):
	materia["IdMateria"] = input("inserisci il numero di materia: ")
	materia["Materia"] = input("inserisci la materia: ")
	file.write("\n"+materia["IdMateria"]+", "+materia["Materia"])