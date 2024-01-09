a=[5,4,8,9,3,1,0]
i=0
for i in range(len(a)):
    i += 1
    j=i
    while j>0:
        if a[i] < a[i-j] : 
            a[i-j] , a[i] = a[i] , a[i-j]
        #print(f"j : {j}")
        j -= 1
    
    #print(f"i : {i}")
    print(a)