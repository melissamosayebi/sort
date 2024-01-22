def selection(a):
    for i in range(len(a)-1):
        j=i
        x=j
        while j<len(a)-1:
            if a[j+1]<a[x]:
                x=j+1
            j+=1
        s=x
        a.insert(i,a[x])
        del a[s+1]
        print(a)
        i+=1
    return a
print(selection([4,5,8,3,6,1,9,7]))
