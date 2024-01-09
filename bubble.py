def bubble(a):
    n=len(a)-1
    i=0
    j=0
    for i in range(len(a)):
        for j in range(n):
            if a[j+1] < a[j]:
                a[j] , a[j+1] = a[j+1] , a[j]
            j += 1
        i += 1  
    return a    
print(bubble([5,4,8,9,3,1,0]))



