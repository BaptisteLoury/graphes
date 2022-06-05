
from pyparsing import match_previous_expr
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rang = 0

    def find(self):
        if self != self.parent:
            self.parent = self.parent.find()
        return self.parent

def union(x : Node,y : Node):
    link(x.find(),y.find())

def link(x : Node,y : Node):
    if x.rang > y.rang:
        y.parent = x
    else:
        x.parent = y

    if x.rang == y.rang:
        y.rang += 1


def kruskal(matrix):
    # parcourt du triangle inférieur gauche uniquement car graphe non orienté
    sorted_art = get_sorted_aretes(matrix)
    # création d'un Node pour chaque sommet
    nodes = [Node(som) for som in range(len(matrix))]
    retained_art = []

    k = 0
    i = 0

    while k < len(matrix) - 1:
        art = None
        while art is None and i < len(sorted_art):

            temp_art = sorted_art[i]
            i += 1

            if nodes[temp_art[0]].find() != nodes[temp_art[1]].find():
                union(nodes[temp_art[0]],nodes[temp_art[1]])
                art = temp_art

        k += 1
        retained_art.append(art)

    return matrix_from_kruskal(retained_art)



def get_aretes_weight(arete):
    return arete[2]

def get_sorted_aretes(matrix):
    aretes = []
    for som in range(len(matrix)):
        for succ in range(som):
            if matrix[som][succ] != 0:
                aretes.append((som,succ,matrix[som][succ]))
    
    aretes.sort(key=get_aretes_weight)
    return aretes

def get_aretes_in_E(matrix,som,E):
    # ici on considère que la matrice représente un graphe non orienté sans arêtes d'un sommet vers lui-même
    aretes = []
    if som < len(matrix):
        for succ in range(len(matrix[som])):
            if succ in E and matrix[som][succ] > 0:
                aretes.append((som,succ,matrix[som][succ]))
    return aretes

def matrix_from_kruskal(arts):
    # nb sommets = nb arêtes conservées + 1
    matrix = [[0 for art in range(len(arts) + 1)] for tra in range(len(arts) + 1)]
    for art in arts:
        matrix[art[0]][art[1]] = art[2]
        matrix[art[1]][art[0]] = art[2]
    return matrix

def prim_bloated(matrix):
    # tableau des couts d'accès pour chaque sommet
    # on rempli les couts avec le plus grand int possible
    cout = [sys.maxsize] * len(matrix)
    # tableau des arêtes retenues pour accéder à chaque sommet
    # on rempli les arêtes retenues avec une arête par défaut (0,0,0) qui sera éléminée au cours de l'algorithme
    pred = [(0,0,0)] * len(matrix)

    cout[0] = 0
    
    # file de priorité avec tous les sommets
    # on commencera par 0
    file = [som for som in range(len(matrix))]

    # tant que la file n'est pas vide
    while len(file) > 0:

        # on récupère et on enlève le premier élément de la liste
        som = file.pop(0)

        # on récupère les aretes de som sous la forme (som,succ,poids) et on les parcourt
        for art in get_aretes_in_E(matrix,som,file):

            # art[0] = som, art[1] = successeur, art[2] = poids
            succ = art[1]

            # si le coût actuel du successeur est >= au poids de l'arête
            if cout[succ] >= art[2]:
                # alors on défini une nouvelle arête d'accès et un nouveau cout d'accès pour le sommet
                pred[succ] = art
                cout[succ] = art[2]

        # on trie la file en fonction du cout des sommets restants
        file.sort(key=lambda x: cout[x])

    # transforme le tableau d'aretes pred en une matrice
    # on ignore la première arrête
    return matrix_from_kruskal([pred[art] for art in range(1,len(pred))])

def prim(matrix):
    selected = [False] * len(matrix)
    k = 0

    selected[0] = True
    retained_art = []

    while k < len(matrix) - 1:
        min = sys.maxsize
        a = 0
        b = 0
        for som in range(len(matrix)):
            if selected[som ]:
                for succ in range(len(matrix)):
                    if not selected[succ] and matrix[som][succ] != 0 and min > matrix[som][succ]:
                        a = som
                        b = succ
                        print(a,b,min,matrix[som][succ])
                        min = matrix[som][succ]

        
        retained_art.append((a,b,min))
        selected[succ] = True
        k += 1
    
    print(retained_art)
    return matrix_from_kruskal(retained_art)

        