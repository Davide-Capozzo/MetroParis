from datetime import datetime

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMapFermate = {}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def buildGraph(self):
        self._grafo.clear() #svuoto prima il grafo
        self._grafo.add_nodes_from(self._fermate) #voglio popolare il mio grafo con la lista di oggetti fermate

        #tic = datetime.now()
        #self.addedges()
        #toc = datetime.now()
        #print("Tempo impiegato da modo 1:", toc-tic)

        #tic = datetime.now()
        #self.addedges2()
        #toc = datetime.now()
        #print("Tempo impiegato da modo 2:", toc - tic)

        tic = datetime.now()
        self.addedges3()
        toc = datetime.now()
        print("Tempo impiegato da modo 3:", toc - tic)

    def get_numnodi(self):
        return len(self._grafo.nodes())  #verifico il numero di nodi

    def get_numarchi(self):
        return len(self._grafo.edges()) #verifico il numero di archi

    #def addedges(self): #verifico che due nodi abbiamo una connessione.
        self._grafo.clear_edges()
        for u in self._fermate: #se si, aggiungo un ramo tra i due
            for v in self._fermate:
                if DAO.hasconn(u,v):
                    self._grafo.add_edge(u, v)


    #addedges però ci mette troppo tempo. possiamo creare un'altra funz.

    #def addedges2(self):
        #self._grafo.clear_edges()

        #for u in self._fermate:
            #for conn in DAO.getvicini(u):
                #v = self._idMapFermate[conn.id_stazA]
                #self._grafo.add_edge(u, v)

    #altro modo per addare edges, più veloce

    def addedges3(self):
        self._grafo.clear_edges()
        alledges = DAO.getAllEdges()
        for conn in alledges:
            u = self._idMapFermate[conn.id_stazP]
            v = self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)

    @property
    def fermate(self):
        return self._fermate