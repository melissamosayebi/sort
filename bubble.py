a=[2,5,4,8,3,7,9,1,0]
j=1
while j!=len(a)-1:
    i=0
    for i in range(len(a)-j):
        if a[i+1]<a[i]:
            a[i] , a[i+1] = a[i+1] , a[i]
        else:
            pass
        #print(a)
        i+=1
    print(j,a)
    j+=1
a[0] , a[1] = a[1] , a[0]
print(j,a)
    
