max_record = 10
num=int(input("Inserisci numero di matricole: "))

if num > max_record:
	print("superato numero massimo di matricole possibili")
	exit()

file = open("MATRICOLE.txt", "w+")
file.write("IdMatricola, Cognome, Nome")

matricola=dict()

for persona in range(num):
	matricola["IdMatricola"] = input("inserisci il numero di matricola: ")
	matricola["Cognome"] = input("inserisci il cognome della matricola: ")
	matricola["Nome"] = input("inserisci il nome della matricola: ")
	file.write("\n"+matricola["IdMatricola"]+", "+matricola["Cognome"]+", "+matricola["Nome"])

