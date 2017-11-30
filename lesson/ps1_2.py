s = 'bobanilobobobobob'
bobs=0
kevin=''
a=''
b=''
c=''
bano=''
for kevin in s:
    a=b
    b=c
    c=kevin
    bano=a+b+c
    if bano=='bob':
        bobs+=1
print("Number of times bob occurs is: "+str(bobs))
    