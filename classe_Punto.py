#programma che simula un piano cartesiano e sia in grado di calcolare la distanza
#tra i punti e vedere se i punti sono sugli assi e in caso su quale asse
import math 

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def isAscissa(self):
        if self.y==0:
            return True
        else:
            return False
        
            
    def isOrdinata(self):
        if self.x==0:
            return True
        else:
            return False
            
    def distanza(self,secondoPunto):
        primoTermine = (self.x-secondoPunto.x)**2
        secondoTermine = (self.y-secondoPunto.y)**2
        distanza = math.sqrt(primoTermine+secondoTermine)
        print(distanza)
        
        
if __name__=="__main__":
    primoPunto=Punto(2,3)
    secondoPunto=Punto(1,1)
    primoPunto.distanza(secondoPunto)
    primoPunto.isOrdinata()
    if primoPunto.isOrdinata()==True:
        print("il punto si trova sull'asse y")
    else:
        print("il punto non si trova sull'asse y") 
    secondoPunto.isOrdinata()
    if primoPunto.isOrdinata()==True:
        print("il punto si trova sull'asse y")
    else:
        print("il punto non si trova sull'asse y") 
    primoPunto.isAscissa()
    if primoPunto.isAscissa()==True:
        print("il punto si trova sull'asse x")
    else:
        print("il punto non si trova sull'asse x") 
    secondoPunto.isAscissa()
    if secondoPunto.isAscissa()==True:
        print("il punto si trova sull'asse x")
    else:
        print("il punto non si trova sull'asse x") 