#ESERCIZIO 1
#1. Crea una lista chiamata numeri con i numeri da 1 a 5. Stampa il terzo elemento (indice 2).
#2. Modifica il secondo elemento di numeri in 10. Stampa la lista aggiornata.
#3. Aggiungi il numero 6 alla fine della lista usando append. Stampa la lunghezza della lista.
#4. Crea una lista mista con 3 stringhe e 2 numeri. Stampa l'ultimo elemento (usa len per calcolarlo).
numeri=[1,2,3,4,5]
print(numeri[2])

numeri[1]=10
print(numeri)

numeri.append(6)
print(len(numeri))

lista=["ksenia","sara","chiara",2,4]
print(lista[len(lista)-1])

#ESERCIZIO 2
#1. Data la lista colori = ["rosso", "blu", "verde", "giallo", "nero"], estrai i primi due colori con slicing.
#2. Estrai gli ultimi tre colori.
#3. Inserisci "bianco" all'indice 1. Stampa la lista.
#4. Rimuovi "verde" e stampa la lunghezza della lista aggiornata.
colori=["rosso","blu","verde","giallo","nero"]
print(colori[0:2])

print(colori[2:5])

colori.insert(1,"bianco")
print(colori)

colori.remove("verde")
print(len(colori))

#ESERCIZIO 3
#1. Usa range(10) in un ciclo for per stampare i numeri da 0 a 9.
#2. Stampa i numeri da 5 a 15 (inclusi 5, escluso 16).
#3. Stampa i multipli di 3 da 0 a 30 usando step=3.
#4. Crea un ciclo che stampi "Ciao" 7 volte usando range.

#print(list(range(5))) genera numeri fino a 5
#print(list(range(0,7))) start e stop da 0 fino a 7 escluso
#print(list(range(0,7,2))) incrementa di 2

for i in range(10):
    print(i)
    
for i in range(5,16):
    print(i)

for i in range(0,31,3):
    print(i)
    
for i in range(0,8):
    print("Ciao")
    
#ESERCIZIO 4
#1. Data città = ["Roma", "Milano", "Napoli", "Torino"],usa un ciclo con range(len(città))
# per stampare ogni città con il suo indice.
#2. Crea una lista di 5 numeri. Usa un ciclo per raddoppiare ciascun numero e stampa la lista modificata.
#3. In una lista di stringhe, usa un ciclo per aggiungere "!" alla fine di ciascuna (es. "ciao" -> "ciao!").
#4. Crea una lista vuota, poi usa un ciclo con range(5) per aggiungere numeri da 1 a 5 con append.
città=["Roma", "Milano", "Napoli", "Torino"]
for i in range(len(città)):
    print(f"città all'indice {i}: {città[i]}")
    
numeri=[1,3,4,5,6]
for i in range(len(numeri)):
    numeri[i] =numeri[i] *2
print(numeri)

parole=["Ciao","Buongiorno","Buonasera","Arrivederci"]
for i in range(len(parole)):
    parole[i] = parole[i] + "!"
print(parole)

lista=[]
for i in range(5):
    lista.append(i+1)
print(lista)

#ESERCIZIO 5
#1. Crea una lista di 10 numeri casuali (usa range per generarli). Calcola la somma con un ciclo.
#2. Filtra una lista: data [10, 15, 20, 25, 30], crea una nuova lista solo con numeri > 20 usando un ciclo e if.
#3. Genera una lista di quadrati da 1 a 10 (es. [1, 4, 9, ...]) con range e append.
#4. In una lista di nomi, usa un ciclo per stampare solo quelli che iniziano con "A" (usa if e slicing).
import random
lista=[]
somma=0
for i in range(10):
    numeri=random.randint(0,10)
    lista.append(numeri)
    somma=somma+lista[i]
print(lista)
print(somma)

lista2=[10,15,20,25,30]
lista3=[]
for i in range(len(lista2)):
    if lista2[i]>20:
        lista3.append(lista2[i])
print(lista3)

quadrati=[]
for i in range(1,11):
    quadrato=i**2
    quadrati.append(quadrato)
print(quadrati)

nomi=["Sofia","Alberto","Alice","Paola","Anna"]
for i in range(len(nomi)):
    if nomi[i][0:1]=="A":
        print(nomi[i])
        
#Livello base: Scrivi un programma che genera una lista di multipli di un numero dato (es. multipli di 5 fino a 50).
#Livello avanzato: Simula un registro di classe: lista di nomi studenti, usa ciclo per assegnare
#voti casuali (con range) e calcola la media classe.
#PRIMO
lista=[]
numero=4
for i in range(4,40,4):
    lista.append(i)
print(lista)
#SECONDO
studenti=["Sara","Chiara","Ksenia","Mattia","Sofia"]
voti=[]
somma=0
for i in range(len(studenti)):
    voto=random.randint(0,10)
    voti.append(voto)
    somma=somma+voto
    print("Studente:",(studenti[i]), "Voto:",(voti[i]))
media=somma/len(studenti)
print("la media dei voti è:", media)









