def fin(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib=[1,1]
        i=2
        while (i<=n):
            fib.append(2*fib[i-1]-fib[i-2])
            i=i+1
        return fib[i-1]
n=int(input("Podaj liczbe: "))


print(fin(n))