import numpy as np

def fun(x,y):
    g=np.ones([x+1,y+1])
    for i in range(x+1):
        for k in range(y + 1):
            if (k==0 or k==i):
                g[i][k]=1
            else:
                g[i][k]=(g[i-1][k-1]+g[i-1][k])
    return  g[x][y]
x=int(input("Podaj 1 wartość: "))
y=int(input("Podaj 2 wartość: "))
if (x<y):
    print("Górna wartość musi być większa od dolnej,")
    print("Rozwiązanie dla ",y," nad ",x)
    print(fun(y,x))
else:print(fun(x,y))