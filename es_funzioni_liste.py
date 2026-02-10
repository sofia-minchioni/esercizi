#problema: data una serie di 10 misurazioni randomiche intere, comprese tra 2 intervalli
#forniti da tastiera produrre in output un file di testo che abbia i valori, la media di valori
#sopra una certa soglia fissata a massimo delle misurazioni meno 10

#sottoproblemi:
#1)creare una lista di 10 misurazioni rando(procedura, perche le liste sono passati per riferimento)
#2)media dei valori di una lista(funzione)
#3)calcolare la soglia [massimo della lista - 10] (funzione)
#4)contare il numero di valori sopra la soglia(procedura)
import random
def creaLista(lista):
    n1=input("inserire il primo estremo ")
    n1=int(n1)
    n2=input("inserire il secondo estremo ")
    n2=int(n2)
    for i in range (0,10):
        if n2>n1:
            valori=random.randint(n1,n2)
        else:
            valori=random.randint(n2,n1)
        lista.append(valori)
        
def calcolo_media(lista):
    somma=0
    for i in range(0,len(lista)):
        somma=somma+lista[i]
    media=somma/len(lista)
    return(media)
    
    
if __name__=="__main__":
    listaM=[]
    creaLista(listaM)
    mediaValori=calcolo_media(listaM)
    





























