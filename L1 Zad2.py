n=0
while n<=0:
    n=int(input("Podaj ilość liczb n: "))
u = 0
i = 0
for i in range(n):
    a = int(input("Wprowadź liczbe: "))
    if a<0:
        u=u+1
        i=i+1
    else: i=i+1
print("Liczb ujemnych jest: ",u)
