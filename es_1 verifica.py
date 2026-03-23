#PROBLEMA 1
def massa_molare(formula):
    if formula=="H2O":
        return 18
    if formula=="NaCl":
        return 58.5
    if formula=="CO2":
        return 44
    return 0

def moli_da_massa(massa_g, formula, unita="g"):
    moli=massa_g/massa_molare(formula)
    return(moli)

def massa_da_moli(moli, formula):
    massa_g=moli*massa_molare(formula)
    return(massa_g)

def stampa_confronto(formula1,massa1,formula2,massa2):
    moli1=moli_da_massa(massa1,formula1)
    moli2=moli_da_massa(massa2,formula2)
    if moli1>moli2:
        print(formula1+" ha più moli")
        differenza1=moli1-moli2
        print("La differenza delle moli è "+str(differenza1))
    else:
        print(formula1+" ha più moli")
        differenza2=moli2-moli1
        print("La differenza delle moli è "+str(differenza2))

if __name__=="__main__":
    moli=moli_da_massa(90,"H2O")
    print(moli)
    grammi=massa_da_moli(1.5,"CO2")
    print(grammi)
    stampa_confronto("CO2",80,"H2O",56)