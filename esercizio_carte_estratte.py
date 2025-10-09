"""
1) estrarre 3 carte da un mazzo(lista)
[1,2,3,4,5,6,7,8,9,10,J,Q,K]
2)calcolare punteggio usando dizionario associ a ogni carta il suo valore
"""
import random
punteggio=0
mazzo=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]

dizionario={"1":1 ,"2":2 ,"3":3,"4":4,"5":5 ,"6": 6 ,"7":7,"8":8,"9":9,"10": 10,"J": 10,"Q":10,"K":10}

carte_estratte = random.sample(mazzo,3)

for i in range(1,3):
   punteggio=punteggio+dizionario[carte_estratte[i]]
    



#" 2 modo"
#import random

#mazzo=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]


#indice =random.randint(1,13)
#carta_estratta = mazzo[indice]


