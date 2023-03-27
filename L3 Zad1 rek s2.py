a=int(input("podaj a: "))
b=int(input("podaj b: "))
def nwd(a,b):
    if b!=0:
        return nwd(b,a%b)
    return a



print(nwd(a,b))