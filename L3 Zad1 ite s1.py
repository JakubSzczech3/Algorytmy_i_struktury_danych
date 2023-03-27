a=int(input("podaj a: "))
b=int(input("podaj b: "))
def nwd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a;
print(nwd(a,b))