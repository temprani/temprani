import sys
a=sys.argv[1:]
k={}
for i in a:
    b=i.split(':')
    key=b[0]
    value=b[1]
    k['key']=value
    print('ID:',key,"Name:",value)
