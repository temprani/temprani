import sys
Income=sys.argv[1:]
global Incomf
Incomf=0

def InOut(a,b):       #接收a,b，打印
    print(a,':',b)

def InCal(c):          #接收一个数据计算实际收入
    try:
        In=int(c)
        if In < 3500:
            PayTax=0
        else:
            if In-3500<1500:
                Rate=0.03
                Min=0
            elif In-3500<4500:
                Rate=0.10
                Min=105
            elif In-3500<9000:
                Rate=0.20
                Min=555
            elif In-3500<35000:
                Rate=0.25
                Min=1005
            elif In-3500<55000:
                Rate=0.30
                Min=2755
            elif In-3500<80000:
                Rate=0.35
                Min=5505
            else:
                Rate=0.45
                Min=13505
        PayTax=(In-3500-In*0.165)*Rate-Min
        Incomf=In-In*0.165-PayTax
        return Incomf

    except:
        print('Error:',c)

for an in Income:
    InCal(an.split(':')[1])
    InOut(an.split(':')[0],Incomf)
