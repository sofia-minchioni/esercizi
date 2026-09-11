#programma che gestisce nome, cognome,età di due persone

nome_prima = "Tommaso"
cognome_prima = "STRA"
eta_prima = 25
lavoro_prima = "insegnante"

nome_seconda = "Luigi"
cognome_seconda = "Rossi"
eta_seconda = 28
lavoro_seconda = "muratore"

print("Età prima persona")
print(eta_prima)
print("Età seconda persona")
print(eta_seconda)

#uso degli oggetti

class Persona:
    def __init__(self,nome,cognome,eta,lavoro):
        self.nome = nome #self è il puntatore ad istanza corretta lo metto sempre davanti
        self.cognome = cognome
        self.eta = eta
        self.lavoro = lavoro
    def stampaEta(self):
        print(self.eta)
    def stampaLavoro(self):
        print(self.lavoro)
    def stampaM(self):
        if self.eta<18:
            print("è minorenne")
        else:
            print("è maggiorenne")
        
prima_persona = Persona("Tommaso","STRA",25,"insegnante")#istanza(tutta la classe con i suoi oggetti e attributi) della persona che contiene la classe,specifico oggetto dell'istanza persona
seconda_persona = Persona("Luigi","Rossi",28,"muratore")
prima_persona.stampaEta()
seconda_persona.stampaEta()
prima_persona.stampaLavoro()
seconda_persona.stampaLavoro()
prima_persona.stampaM()
seconda_persona.stampaM()
