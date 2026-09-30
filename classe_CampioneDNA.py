class CampioneDNA:
    """
    questa classe rappresenta un campione di DNA, tracciandone la sequenza nucleotidica, i geni identificati
    e un registro delle mutazioni rilevate nel tempo
    """
    def __init__(self,__codice_campione,__sequenza,__geni_mappati,__mutazioni_rilevate,laboratorio):
        """
        inizializza una nuova istanza della classe DNA
        """
        self.__codice_campione=__codice_campione
        self.__sequenza=__sequenza.upper()
        self.__geni_mappati=__geni_mappati
        self.__mutazioni_rilevate=__mutazioni_rilevate
        self.laboratorio=laboratorio
    
    def aggiungi_gene(self,gene):
        """
        aggiunge un nuovo gene alla lista solo se esso non è già presente all'interno della lista
        per evitare duplicati
        """
        if gene in self.__geni_mappati:
            print("il gene è gia presente")
        else:
            self.__geni_mappati.append(gene)
            print("il gene è stato aggiunto")

    def registra_mutazioni(self,posizione,tipo_mutazione):
        """
        inserisce o aggiorna una mutazione nel dizionario __mutazioni_rilevate
        """
        self.__mutazioni_rilevate[posizione]=tipo_mutazione
        print("la mutazione è stata aggiunta")

    def calcola_percentuale_gc(self):
        """
        calcola la percentula di basi Guanina(G) e Citosina(C) all'interno della sequenza
        """
        G=self.__sequenza.count("G")
        C=self.__sequenza.count("C")
        somma_basi=G+C
        percentuale=(somma_basi/len(self.__sequenza))*100
        return(percentuale)

    def stampa_report(self):
        """
        permette di stampare a video la scheda riassuntiva con i dati del campione
        """
        print("--scheda riassuntiva dati campione--")
        print("codice: ",self.__codice_campione)
        print("laboratorio: ",self.laboratorio)
        print("sequenza: ",self.__sequenza)
        print("geni mappati: ",self.__geni_mappati)
        print("mutazioni: ",self.__mutazioni_rilevate)

if __name__=="__main__":
    listaGeni=["geneA","ampR2","lacZ"]
    dizionarioMutazioni={45:"sostituzione", 120:"delezione"}
    campioneUno=CampioneDNA("DNA-4029","ATCGGCTA", listaGeni,dizionarioMutazioni,"LabGen-BioApp")
    campioneUno.aggiungi_gene("geneA")
    campioneUno.registra_mutazioni(45, "sostituzione")
    campioneUno.calcola_percentuale_gc()
    print(campioneUno.stampa_report())
    

    