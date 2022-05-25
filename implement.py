from ast import IsNot
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


def var_dump_table(table): # afficher une matrice 
    i = 0
    for e in table:
        print(i,e)
        i+=1


def parcourir_graphe_profondeur(graphe):
    parcouru=[] #tableau qui permet de contenir les sommets déjà étudiés.
    
    
    
    sommet=0 # on commence par le premier sommet
   
    while not (len(parcouru)==len(graphe)): #Pour chacun des sommets tant qu'ils ne sont pas déjà étudiés
        if sommet in parcouru: #s'il a déjà été étudié on change de sommet
            sommet+=1
        else: #s'il n'a pas été étudié encore 
            parcouru.append(sommet) # on ajoute le sommet dans le tableau des sommets parcourus
            #present=False
            for j in graphe[sommet]: # on parcours les successeurs du sommet étudié
                if j not in parcouru:
                        parcouru.append(j)

    return parcouru            
        



def matrix_with_index(matrix):
    return [(i,matrix[i]) for i in range(len(matrix))]
