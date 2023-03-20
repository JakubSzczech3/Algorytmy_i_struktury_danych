tablica=[2,3,4,5]
a=int(input("wprowadź a: "))
i=0
x=0
for i in range(4):
    if tablica[i]==a:
        print("Wartość występuje w tablicy")
        i=i+1
    else: x=x+1
if x==4:
    print("Wartość nie występuje w tablicy")