#esercizio equazioni secondo grado
import math

def AcquisisciCoefficenti():
    global a,b,c
    a=float(input("inserisci il valore del coefficiente a: "))
    b=float(input("inserisci il valore del coefficiente b: "))
    c=float(input("inserisci il valore del coefficiente c: "))
    
def CalcolaDelta():
        global a,b,c,d
        d=(b*b)-(4*a*c)
        
def VisualizzaSoluzioni():
    global a,b,c,d,x1,x2
    if(d<0):
        print("L'equazione non ammette soluzioni reali")
    else:
        x1=(-b - math.sqrt(d))/(2*a)
        x2=(-b + math.sqrt(d))/(2*a)
        print("x1=",x1,"x2=",x2)

def RisolviEquazione():
    global b,c,x1
    if((b==0)and(c==0)):
        print("Equazione indeterminata")
    else:
        if(b==0):
            print("Equazione impossibile")
        else:
            x1=float(-c)/float(b)
            print("x=",x1)
AcquisisciCoefficenti()
if(a!=0):
    CalcolaDelta()
    VisualizzaSoluzioni()
else:
    RisolviEquazione()
        
        
