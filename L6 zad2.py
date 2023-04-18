a=int(input("Podaj a: "))
b=int(input("Podaj b :"))

if a<b:
    while a<b:
        if a%2==0:
            print(a)
            a=a+1
        else:
            a=a+1

else:
    print("Błędny zakres wartości")