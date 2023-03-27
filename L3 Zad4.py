a=int(input("podaj liczbe do konwersji: "))
def bin(a):
   if a>1:
       bin(a//2)
   print(a%2,end="")

print(bin(a))
