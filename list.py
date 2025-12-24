import copy

lst=[10,20,30,40,50,10,20,11]
uniq=[]
evn=[]
for x in lst:
    if x not in uniq:
        uniq.append(x)
    print("without duplicate",uniq)

    if x%2==0:
        evn.append(x)
    print("even",evn)

    lst.sort()
    print(lst[-2])

nested=[[1,2,3],[4,5,6],[7,8,9]]
print(nested)
for y in nested:
    print(sum(y))

original=[[10,20],[30,40]]
shallow=original.copy()
deep=copy.deepcopy(original)
original[0][0]=99
print(original)
print(shallow)
print(deep)


