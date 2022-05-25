import numpy as np

# graphe = [[1,2], [2], [3], [4], []]
# graphe=[[0,2,3,4],[1,2,4],[0,2,3,4],[1,2,3,4],[0,2,4]]
# graphe=[[4,6,8,9],[1,2,7,9],[0,2,9],[1,4,5,6,8,9],[1,8,9],[3,4,6,9],[2,3,5,6,8,9],[3,4,5,6,8,9],[0,1,3,6,8,9],[0,1,2,5,7,9]]
graphe=[[0,1,2,6,7,9],[1,8,9],[1,3,5,8,9],[0,2,3,4,6,9],[1,3,4,7,9],[1,4,9],[4,6,7,9],[1,2,5,9],[0,3,5,6,9],[2,5,9]]


def calc_matrice_adj(graphe):
    card = len(graphe)
    matrice = [[0 for x in range(card)] for y in range(card)]
    for x in range(card):
        for y in range(card):
            if y in graphe[x]:
                matrice[x][y] = 1

    return matrice

def roy_warshall_for_matrice(matrix):
    card = len(matrix)
    for a in range(card): # pour chaque sommet
        for b in range(card): # pour chacun de ses predecesseurs
            if matrix[b][a] == 1:
                for c in range(card): # pour chaqun des successeurs de a
                    if matrix[a][c] == 1:
                        matrix[b][c] = 1
    return matrix

def roy_warshall_for_list_of_list(graphe):
    card = len(graphe)
    for a in range(card): # pour chaque sommet
        y = 0
        for predecesseurs in graphe: 
            if a in predecesseurs: # si a est un predecesseur alors
                for successeurs in graphe[a]:
                    graphe[y].append(successeurs)
            y += 1
    return remove_doublons(graphe)

def remove_doublons(graphe):
    no_doublon_graphe = []
    for row in range(len(graphe)):
        no_doublon_graphe.append([])
        for e in graphe[row]:
            if e not in no_doublon_graphe[row]:
                no_doublon_graphe[row].append(e)
    return no_doublon_graphe


def var_dump_table(table):
    i = 0
    for e in table:
        print(i,e)
        i+=1


# Séance 1
matrix = calc_matrice_adj(graphe)
print("Matrice d'adjacence")
var_dump_table(matrix)
print("Matrice de Roy Warshall (matrice)")
matrix = roy_warshall_for_matrice(matrix)
var_dump_table(matrix)
# print("Matrice de Roy Warshall (list of list)")
# graphe = roy_warshall_for_list_of_list(graphe)
# var_dump_table(graphe)