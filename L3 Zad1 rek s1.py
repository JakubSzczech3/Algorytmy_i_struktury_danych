a=int(input("podaj a: "))
b=int(input("podaj b: "))
def nwd(a,b):
    if a==b:
        return a
    elif a>b:
        a=a-b
        return nwd(a,b)
    else:
        b=b-a
        return nwd(a, b)
print(nwd(a,b))