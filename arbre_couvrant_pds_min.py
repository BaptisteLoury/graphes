
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rang = 0

    def find(self):
        if self != self.parent:
            self.parent = self.parent.find()
        return self.parent

def union(x,y):


def link(x,y):
    

def kruskal(matrix):
    # parcourt du triangle inférieur gauche uniquement car graphe non orienté
    sorted_art = get_sorted_aretes(matrix)
    nodes = [Node(som) for som in range(len(matrix))]

    k = 0
    i = 0

    while k < len(matrix):
        art = None
        while art is None and i < len(sorted_art):
            if nodes[art[0]].find() == nodes[art[0]].find():
                print("aled")

    return []

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


def prim(matrix):
    return []