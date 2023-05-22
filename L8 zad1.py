import random

def b(tab,x,l,p):
    while l<=p:
        m=l+(p-l)//2

        if tab[m]==x:
            print (m)
            exit()
        elif tab[m]<x:
            l=m+1
        else:
            p=m-1
    print("Nie znaleziono")

tab=[]
for i in range (10):
    tab.append(random.randint(-100,100))

print(tab)
tab.sort()
print(tab)

x=int(input("Podaj x: "))

b(tab,x,0,len(tab)-1)