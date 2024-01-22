a=[4,6,3,8,7,9,1]
i=1
for i in range(len(a)):
    j=i-1
    x=i
    while j!=-1:
        if a[i]<a[j]:
            x=j
        j-=1
    a.insert(x,a[i])
    del a[i+1]
    print(a,x,i)
    i+=1
print(a)

