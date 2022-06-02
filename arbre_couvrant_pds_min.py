
from pyparsing import match_previous_expr


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

def matrix_from_kruskal(arts):
    # nb sommets = nb arêtes conservées + 1
    matrix = [[0 for art in range(len(arts) + 1)] for tra in range(len(arts) + 1)]
    for art in arts:
        matrix[art[0]][art[1]] = art[2]
        matrix[art[1]][art[0]] = art[2]
    return matrix

def prim(matrix):
    return []