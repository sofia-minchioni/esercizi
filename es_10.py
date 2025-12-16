#scrivere un programma che generi una lista di numeri
#casuali compresi tra 1,100 che rappresentano misurazioni di intensità
#di un segnale. Il programma dopo aver generato la lista deve essere in
#grado di modificarla in questa maniera :gli elementi di indice pari
#devono essere azzerati. Inoltre , dopo la modifica, si vuole contare il numero
#di elementi sopra una soglia numerica.

#sottoproblemi :
#1) generare una lista di numeri compresi tra 1 e 100 .
#2) modificare la lista con la regola sopra
#3) contare il numero di elementi sopra la soglia
import random 

def generaLista(n):
    myList=[]
    for i in range (0,n):
        elemento=random.randint(1,100)
        myList.append(elemento)
    return myList

#def proceduraGeneraLista(n,lista):
#    for i in range (0,n):
#       elemento=random.randint(1,100)
#       myList.append(elemento)
    
def modificaLista(n,lista):
    n=len(lista)
    for i in range(0,n):
        if i%2==0:
            lista[i]=0
            
def sogliaIteratore(lista,nsoglia):
    contatore=0
    for element in lista:
        if element>nsoglia:
            contatore=contatore+1
    return(contatore)
        


listax=generaLista(6)
#listap=[]
#proceduraGeneraLista(6,listap)
#proceduraGeneraLista(lista=listap,n=6)
modificaLista(6,listax)
nsoglia = sogliaIteratore (listax,50)


    