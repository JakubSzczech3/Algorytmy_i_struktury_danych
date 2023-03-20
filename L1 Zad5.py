tab=[[9,3],[9,7]]
j=0
for j in range(2):
    i=0
    g=0
    min=tab[j][0]
    for i in range(2):
        if tab[j][i]<min:
            min=tab[j][i]
            g=i
            i=i+1
        else: i=i+1
    tab[j][g]=tab[j][0]
    tab[j][0]=min
    j=j+1
print(tab)