a=[4,5,8,9,3,1,0]
n=len(a)-1
i=0
for i in range(len(a)):
    f=len(a)-i
    min=a[i]
    j=1
    while j<f :
        if min<a[i+j]:
            min = min
        else:
            min = a[i+j]
        print(f"j : {j}")
        a[i] , min = min , a[i]
        j += 1
        #print(f"j : {j}")
    #print(f"i : {i}")
    i+=1
    print(i,min,a,j)
