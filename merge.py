def sorting(a,b):
    len1=len(a)
    len2=len(b)
    c=[]
    i=0
    j=0
    while i<len2 and j<len1:
        if b[i]<a[j]:
            c.append(b[i])
            i+=1
        else:
            c.append(a[j])
            j+=1
    if len(a)>0 or len(b)>0:
        c=c+a[j:]+b[i:]
    return c
def cel(_list):
    if len(_list)==1:
        return _list
    else:
        mid=len(_list)//2
        left=_list[0:mid]
        right=_list[mid:]
        #print(f"l is {left}",f"r is {right}")
    left=cel(left)
    right=cel(right)
    return sorting(left,right)
print(cel([2,7,3,6,0,4,1]))