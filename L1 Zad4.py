tablica=[2,3,5,5]
i=0
min=tablica[0]
for i in range(4):
    if tablica[i]<min:
        min=tab[i]
        i=i+1
    else: i=i+1
print("Najmniejsza wartość: ",min)
