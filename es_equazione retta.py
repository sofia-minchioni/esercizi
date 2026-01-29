#scrivere un programma che dati due punti in un piano cartesiano
#scriva l'equazione della retta associata e mandi in output
#il messaggio con la positività o negatività del coefficente angolare

#sottoproblemi
#1)calcolare il coefficiente angolare(funzione)(4parametri xUno,xDue,yUno,yDue)
#2)calcolare l'equazione della retta tramite il fascio(procedura)(3parametri m,xDue,yDue)
import random

def calcolo_m(xuno,xdue,yuno,ydue):
    m=(ydue-yuno)/(xdue-xuno)
    return(m)#rilascia m all'esterno,quando finisce ho 0 variabili, perche esistono solo qua dentro

def equazione(m,x,y):
    eq="y-"+str(y)+"="+str(m)+"(x-"+str(x)+")"#concatenazione di stringhe fisse e variabili, il + serve ad unirle
    print(eq)
    
def controllo_m(m):
    if m>0:
        print("m ha segno positivo")
    elif m==0:
        print(" m è nullo")
    else:
        print("m ha segno negativo")
#esempio incremento        
def incremento_uno(a):
    a=a+1
    print(a)

def incremento_uno_stable(a):
    a=a+1
    return(a)

if __name__=="__main__":
    xuno=random.randint(-20,20)
    xdue=random.randint(-20,20)
    yuno=random.randint(-20,20)
    ydue=random.randint(-20,20)
    
    coefficiente_angolare=calcolo_m(xuno,xdue,yuno,ydue)
    print(coefficiente_angolare)
    equazione(coefficiente_angolare,xdue,ydue)#gli passo le variabili che ho definito nel main    
    controllo_m(coefficiente_angolare)
    incremento_uno(xuno)#i numeri qua dentro non cambiano perche passano per valore,le liste cambiano 
    xuno= incremento_uno_stable(xuno)#in questo caso il valore cambia perche l'ho sovrascritto,l'ho riassegnata


