def sommaLista (lista):
    somma=0 # si chiama scop (la variabile somma esiste solo all'interno della funzione)
    for element in lista:
        somma=somma + element
    print(somma)

#scrivere una funzione che data una lista stampi a video il numero degli elementi pari
def pariLista (lista):
    sommapari=0
    for element in lista:
        if element%2==0:
            sommapari=sommapari+1
    print(sommapari)

lista=[1,2,3,4]
sommaLista(lista)
pariLista(lista)
#ho richiamato la funzione sommaLista, quello dentro le parentesi si chiama parametro
lista2=[2,3,4,5]
sommaLista(lista2)

