#scrivere un programma che dati due numeri
#interi random in un intervallo 0,100 ne calcoli
#la somma,ne calcoli la differenza e controlli
#se la differenza è minore di una certa soglia fissata a priori
#nel main
#sottoproblemi:
#1)somma di due numeri(procedura, perche poi non mi serve più)
#2)differenza tra due numeri(funzione)
#3)verificare se un numero è minore di una soglia(procedura)
import random

def proceduraCalcoloSommaNumeri(numero_uno,numero_due):
    somma=numero_uno+numero_due
    print(somma)
    
def funzioneCalcoloDifferenzaNumeri(numero_uno,numero_due):
    differenza = numero_uno-numero_due
    return(differenza) 

def proceduraVerifica(differenza,soglia=25):
    if differenza<soglia:
        print("la differenza è minore della soglia")
    else:
        print("la differenza è maggiore della soglia")

if __name__=="__main__":
    a=random.randint(0,100)
    b=random.randint(0,100)
    proceduraCalcoloSommaNumeri(a,b)
    diff=funzioneCalcoloDifferenzaNumeri(a,b)
    proceduraVerifica(a,b)
    soglia=25
    

    
    
