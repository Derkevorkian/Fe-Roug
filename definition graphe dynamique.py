import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import numpy as np

class DynamicGraph:
    def initialisationgraphe(graphe):#on represente le graphe sous forme de dictionnaire
        arretes = {}
        elementdynamiques = {'niveaudetrafic': 1}

    def ajoutnoeud(graphe, u, v, fonctioncout"""fonction qui calcul le cout dynamique"""):#ajout d'une arrete de u vers v '
        if u not in arretes:
            arretes[u] = {}
        arretes[u][v] = fonctioncout

    def update_state(graphe, nouveletat):
        niveaudetrafic.update(nouveletat)

    def coutheuredonnee(graphe, u, v, tempsarrivee):
        fonctioncout = arretes[u][v]
        return fonctioncout(tempsarrivee, niveaudetrafic)