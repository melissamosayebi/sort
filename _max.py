c=int(input ("how many ? "))
a=int(input("x : "))
b=int(input("x : "))
if a>b:
      _max=a
else:
      _max=b
while c>2:
    d=int(input("x : "))
    if d>_max:
        _max=d
    else:
        _max=_max
    c-=1
print(_max)
