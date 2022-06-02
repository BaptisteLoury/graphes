from ast import IsNot
from re import finditer
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


def estPossible(graphe, sommet, parcourus):
    for i in graphe(sommet):
        if i not in parcourus:
            return True
    return False


# def parcourir_graphe_profondeur(graphe,sommet_depart):
#     sommets_finis=[]
#     sommets_parcourus=[]
#     while not (len(sommets_parcourus)==len(graphe)):
#         sommet=sommet_depart
#         while not sommet in sommets_finis:
#             while estPossible(graphe,sommet,sommets_parcourus):
#                 for i in graphe(sommet):
#                     if i not in sommets_parcourus:
#                         sommet=i
#                         sommets_parcourus.append(sommet)
#             sommets_finis.append(sommet)
#             # if len(sommets_parcourus)>1:
#             sommet=sommets_parcourus(sommet-1)
#             # else:
#                 # sommet=sommets_parcourus(sommet)
    
#     return sommets_parcourus


def parcourir_graphe_profondeur(graphe,sommet_depart):
    
    aTraiter=[]
    parcouru=[]
    sommet=sommet_depart
    aTraiter.append(sommet)
    while len(aTraiter)!=0:
        sommet=aTraiter[0]
        aTraiter.remove(sommet)
        parcouru.append(sommet)
        
        for i in graphe[sommet]:
            if i not in parcouru and i not in aTraiter:
                aTraiter.append(i)
    return parcouru


                
def determiner_composantes_connexes(graphe):
    composantes_fortement_connexes=[] 
    sommets_restant=[]
    for i in range(len(graphe)):
        sommets_restant.append(i)
    while len(sommets_restant) !=0:
       
        # on observe la propagation des + et on met les sommetes concernés dans une liste
        composante_plus=parcourir_graphe_profondeur(graphe,sommets_restant[0])

        #On cherche la propagation des - et on les met dans une liste
        composante_moins=[sommets_restant[0]]
        sommets_moins_restants=[sommets_restant[0]]
    
        while len(sommets_moins_restants) !=0 :
            
            for x in range(len(graphe)):
                for y in graphe[x]:
                    
                    if sommets_moins_restants[0]==y and  x not in sommets_moins_restants and x not in composante_moins:
                        sommets_moins_restants.append(x)
                        composante_moins.append(x)
            sommets_moins_restants.pop(0)    

        # On prend les sommets marqués par des + et des - et on les met dans la composante fortement connexe
        
        composante_connexe=[]
           
        for k in composante_plus:
            for l in composante_moins:
                if k==l:
                    composante_connexe.append(k)
                    # composante_plus.remove(k)
       #  on ajoute la composante connexe dans notre liste de composantes connexes  
           
        composantes_fortement_connexes.append(composante_connexe)
       
        # supprimer dans les sommets restants, les sommets de la composante fortement connexe
        for sommet in composante_connexe:
            sommets_restant.remove(sommet)

    return composantes_fortement_connexes


def matrice_predecesseur(graphe):
    card = len(graphe)
    matrice = [[0 for x in range(card)] for y in range(card)] #creation d'une matrice de 0
    for a in range(card):
        for b in graphe[a]:
            matrice[b][a]=1
    return matrice



    






def matrix_with_index(matrix):
    return [(i,matrix[i]) for i in range(len(matrix))]
