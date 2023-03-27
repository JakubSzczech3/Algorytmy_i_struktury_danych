def han(a, x, y, g):
    if a == 1:
        print("Przesuń dysk 1 z kijka ", x, "na kijek ", y)
        return
    han(a - 1, x, g, y)
    print("Przesuń dysk ", a, "z kijka ", x, "na kijek ", y)
    han(a - 1, g, y, x)
a=int(input("podaj liczbe krążków: "))
han(a, '1', '2', '3')