tablica = []
for i in range(1,4):
	in1 = int(input("Jaką liczbę dodać?"))
	tablica.append(in1)
suma = 0
for liczby in tablica:
	suma += liczby
if suma==0:
	print("tablica jest pusta")
else:
	print("suma liczb w tablicy wynosi: "+str(suma))
if suma%2 == 0:
	print('suma jest parzysta')
