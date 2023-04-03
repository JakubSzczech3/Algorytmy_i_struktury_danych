def partition(a,l,h):
    p=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<=p:
            i=i+1
            (a[i],a[j])=(a[j],a[i])
    (a[i+1],a[h])=(a[h],a[i+1])
    return i+1;
def quickSort(a,l,h):
    if l<h:
        pi=partition(a,l,h)
        quickSort(a,l,pi-1)
        quickSort(a,pi+1,h)
g=0
tab=[]
m=""
while (1>0):
    m=input("Podaj współżędną wektora (puste kończy wprowadzanie): ")
    if (m==""):
        break
    else:
        m=int(m)
        tab.append(m)
v=len(tab)
quickSort(tab,0,v-1)
print(tab[v-1])
