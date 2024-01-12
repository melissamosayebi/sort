a=[5,0,9,1,8,3,4]
i=0
while i!=len(a):
    j=0
    _min=a[i]
    j=j+i+1
    while j!=len(a):
        if _min<a[j]:
            _min=_min
        else :
            _min=a[j] 
            #print(f"what {a[j]}")
        #print(_min,a[j],j)  
        j+=1
    print(_min)
    a[i] , _min = _min , a[i]
    print(_min,j,f"i is : {i}",a)
    i+=1
    