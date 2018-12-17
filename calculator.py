import sys
try:
    In=int(sys.argv[1])
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
        PayTax=(In-3500)*Rate-Min
    print(format(PayTax,".2f"))
except:
    print('Error:',sys.argv[1])

