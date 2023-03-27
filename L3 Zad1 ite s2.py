a=int(input("podaj a: "))
b=int(input("podaj b: "))
p=0
while b!=0:
    p=b
    b=a%b
    a=p
print("a= ",a)