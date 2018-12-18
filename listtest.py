import sys
a=sys.argv[1:]
bm1=[]
bm2=[]
for i in a:
    if len(i) <=3:
        bm1.append(i)
    if len(i) >3:
        bm2.append(i)
print(bm1)
print(bm2)
