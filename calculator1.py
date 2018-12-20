import sys
Income=sys.argv[1:]
Incomf=0

def InOut(a,b):       #接收a,b，打印
    print(a,':',format(b,'.2f'))

def InCal(c):          #接收一个数据计算实际收入
    try:
        In=int(c)
        YN=In-3500-In*0.165
        if In <= 3500:
            PayTax=0
        else:
            if YN<1500:
                Rate=0.03
                Min=0
            elif YN<4500:
                Rate=0.10
                Min=105
            elif YN<9000:
                Rate=0.20
                Min=555
            elif YN<35000:
                Rate=0.25
                Min=1005
            elif YN<55000:
                Rate=0.30
                Min=2755
            elif YN<80000:
                Rate=0.35
                Min=5505
            else:
                Rate=0.45
                Min=13505
            PayTax=YN*Rate-Min
        global Incomf
        Incomf=In-In*0.165-PayTax
        return Incomf

    except:
        print('Error:',c)

for an in Income:
    InCal(an.split(':')[1])
    InOut(an.split(':')[0],Incomf)
