import random
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