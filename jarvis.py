import random

def riempiTemperature(lista):
    """
    questa funzione rimpe le liste con valori random
    :params lista: lista che si deve riempire
    """
    for i in range(0,24):
        temperature=random.randint(-3,28)
        lista.append(temperature)

def media(lista):
    """
    questa funzione calcola la media di una distribuzione numerica
    
    :params lista: Lista contenente le misurazioni
    """
    somma=0
    for i in range(0,len(lista)):
        somma=somma+lista[i]
    media=somma/24
    return(media)

def varianza(lista,media):
    """
    questa funzione calcola la varianza di una distribuzione numerica
    :params lista: lista contenente le misurazioni
    :params media: media delle distribuzioni
    """
    varianza=0
    for i in range(0,len(lista)):
        v=(lista[i]-media)**2
        varianza=varianza+v
    varia=varianza/24
    return(varia)

def deviazione_standard(varianza):
    """
    questa funzione calcola la deviazione standard di una distribuzione numerica
    :params varianza:
    """
    dev=varianza**0.5
    return(dev)

def giornata_calda(media_temperature):
    """
    questa funzione calcola la giornata più calda di una distribuzione numerica
    :params media_temperature:lista contenente la media di tutte le liste
    """
    
    media_max=media_temperature[0]
    for i in range(0,len(media_temperature)):
        if media_temperature[i]>media_max:
            media_max=media_temperature[i]
        indice=media_temperature.index(media_max)
        if indice==0:
            giorno="lunedi"
        elif indice==1:
            giorno="martedi"
        elif indice==2:
            giorno="mercoledi"
        elif indice==3:
            giorno="giovedi"
        elif indice==4:
            giorno="venerdi"
        elif indice==5:
            giorno="sabato"
        elif indice==6:
            giorno="domenica"
    print("il giorno più caldo è "+ giorno)
    print("La media di temperature piu alta è "+str(media_max))

def giornata_fredda(media_temperature):
    """
    questa funzione calcola la giornata più fredda di una distribuzione numerica
    :params media_temperature:lista contenente la media di tutte le liste
    """
    media_min=media_temperature[0]
    for i in range(0,len(media_temperature)):
        if media_temperature[i]<media_min:
            media_min=media_temperature[i]
        indice=media_temperature.index(media_min)
        if indice==0:
            giorno="lunedi"
        elif indice==1:
            giorno="martedi"
        elif indice==2:
            giorno="mercoledi"
        elif indice==3:
            giorno="giovedi"
        elif indice==4:
            giorno="venerdi"
        elif indice==5:
            giorno="sabato"
        elif indice==6:
            giorno="domenica"
    print("il giorno più freddo è "+ giorno)
    print("La media di temperature piu bassa è "+str(media_min))

def moda(lista):
    """
    questa funzione calcola la moda di una distribuzione numerica
    :params lista: lista contenente le misurazioni
    """
    moda=0
    conteggio_m=0
    for element in lista:
        conto=lista.count(element)
        if conto>conteggio_m:
            conteggio_m=conto
            moda=element
def errore_standard(deviazione_standard):
    """
    questa funzione calcola l'errore standard di una distribuzione numerica
    :params deviazione_standard:
    """
    errore=deviazione_standard/(24**0.5)
    return(errore)

    return(moda)