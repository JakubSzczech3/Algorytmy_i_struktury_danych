def suma(x,y,z):
    if y==z:
        return x[y]
    else:
        g=(y+z)//2
        h=suma(x,y,g)
        j=suma(x,g+1,z)
        return h+j
tablica=[453,23,34,24,342,424,11,1]
k=len(tablica)-1
print(suma(tablica,0,k))