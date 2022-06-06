from ast import IsNot
from re import finditer
import numpy as np
import random as rand

# graphe = [[1,2], [2], [3], [4], []]
# graphe=[[0,2,3,4],[1,2,4],[0,2,3,4],[1,2,3,4],[0,2,4]]
# graphe=[[4,6,8,9],[1,2,7,9],[0,2,9],[1,4,5,6,8,9],[1,8,9],[3,4,6,9],[2,3,5,6,8,9],[3,4,5,6,8,9],[0,1,3,6,8,9],[0,1,2,5,7,9]]
graphe=[[0,1,2,6,7,9],[1,8,9],[1,3,5,8,9],[0,2,3,4,6,9],[1,3,4,7,9],[1,4,9],[4,6,7,9],[1,2,5,9],[0,3,5,6,9],[2,5,9]]

# La fonction calc_matrice_adj permet d'obtenir la matrice d'adjacence du graphe orienté donné en paramètre.
def calc_matrice_adj(graphe):
    card = len(graphe) # on récupère la taille du graphe (soit le nombre de sommets du graphe)
    matrice = [[0 for x in range(card)] for y in range(card)]  # on créer une matrice carré du nombre de sommets et on la remplie de 0
    for x in range(card): #on analyse pour chaque sommet du graphe les successeurs
        for y in range(card):
            if y in graphe[x]:
                matrice[x][y] = 1 # On ajoute dans notre matrice créée le 1 qui signifie que c'est un successeur du sommet parcouru

    return matrice

# La fonction calc_matrice_adj_non_orient permet d'obtenir la matrice d'adjacence du graphe non orienté donné en paramètre.
def calc_matrice_adj_non_orient(graphe):    
    card = len(graphe) # on récupère la taille du graphe (soit le nombre de sommets du graphe)
    matrice = [[0 for x in range(card)] for y in range(card)] # on créer une matrice carré du nombre de sommets et on la remplie de 0
    for x in range(card): #on analyse pour chaque sommet du graphe les successeurs
        for y in range(card):
            if y in graphe[x]:
                matrice[x][y] = 1 # On ajoute dans notre matrice créée le 1 qui signifie que c'est un successeur du sommet parcouru
                matrice[y][x] = 1 # Comme le graphe est non orienté, on ajoute le fait que le sommet est également successeur.

    return matrice

# La fonction ponderation_graphe_non_orient 
def ponderation_graphe_non_orient(matrix):
    matrix_ponderee = matrix 

    for som in range(len(matrix_ponderee)):
        matrix_ponderee[som][som] = 0
        for succ in range(som):
            if matrix_ponderee[som][succ] != 0:
                matrix_ponderee[som][succ] = rand.randint(1,100)
                matrix_ponderee[succ][som] = matrix_ponderee[som][succ]
        
    return matrix_ponderee

# La fonction roy_warshall_for_matrice permet d'obtenir la fermeture transitive à partir d'une matrice
def roy_warshall_for_matrice(matrix):
    card = len(matrix) # on récupère la taille du graphe (soit le nombre de sommets du graphe)
    for a in range(card): # pour chaque sommet
        for b in range(card): # pour chacun de ses predecesseurs
            if matrix[b][a] == 1:
                for c in range(card): # pour chacun des successeurs de a
                    if matrix[a][c] == 1:
                        matrix[b][c] = 1
    return matrix

def roy_warshall_for_list_of_list(graphe):  # La fonction roy_warshall_for_matrice permet d'obtenir la fermeture transitive à partir d'un graphe
    card = len(graphe) # on récupère la taille du graphe (soit le nombre de sommets du graphe)
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

# La procédure var_dump_table permet d'afficher une matrice 
def var_dump_table(table): 
    i = 0
    for e in table:
        print(i,e)
        i+=1

# La fonction parcourir_graphe_profondeur prend en paramètre un graphe et un sommet de départ. Elle parcourt le graphe et retourne un tableau contenant l'ordre  dans lequel les sommets sont parcourus
def parcourir_graphe_profondeur(graphe,sommet_depart):
    
    aTraiter=[] # On initialise un tableau qui contiendra les sommets à analyser
    parcouru=[] # On initialise un tableau qui contiendra les dommets déjà traités pour éviter de les traiter à nouveau.
    sommet=sommet_depart 
    aTraiter.append(sommet) # on ajoute le sommet dans la liste à traiter
    while len(aTraiter)!=0: #tant qu'il y a des sommets  à traiter on continue
        sommet=aTraiter[0] # On s'intéresse au premier sommet de la liste à traiter
        aTraiter.remove(sommet) # on le retire de la liste  à traiter
        parcouru.append(sommet) # on l'ajoute dans la liste des sommets traités
        
        for i in graphe[sommet]: #pour chacun des successeurs du sommet concerné s'ils n'ont pas été parcourus on les ajoute dans la liste à traiter
            if i not in parcouru and i not in aTraiter:
                aTraiter.append(i)
    return parcouru




# La fonction determiner_composantes_connexes permet de trouver les composantes connexes d'un graphe       
def determiner_composantes_connexes(graphe):
    composantes_fortement_connexes=[] 
    sommets_restant=[]
    for i in range(len(graphe)):
        sommets_restant.append(i)
    while len(sommets_restant) !=0:
       
        # on observe la propagation des + et on met les sommets concernés dans une liste
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

# La fonction matrice_predecesseur retourne une matrice des prédécesseurs à partir d'une graphe
def matrice_predecesseur(graphe):
    card = len(graphe) #on récupère la taille du graphe soit le nombre de sommets
    matrice = [[0 for x in range(card)] for y in range(card)] #creation d'une matrice de 0
    for a in range(card):
        for b in graphe[a]:
            matrice[b][a]=1 # on regarde pour chaque sommet ses prédecesseurs et on les ajoute dans la matrice créée
    return matrice


# Retourne la matrice d'un graphe pondéré non orienté sans arrêtes d'un sommet vers lui-même
def generer_graphe_pondere(n,arts):
    # création d'une matrice n*n de 0
    matrice = [[0 for a in range(n)] for b in range(n)]


    for i in range(n-1):
        matrice[i+1][i] = rand.randint(1,1000)

    k = n-1
    while k < arts:
        som = rand.randint(1,n-1)
        succ = rand.randint(0,som-1)
        if matrice[som][succ] == 0:
            matrice[som][succ] = rand.randint(1,1000)
            matrice[succ][som] = matrice[som][succ]
            k += 1

    return matrice

def matrix_with_index(matrix):
    return [(i,matrix[i]) for i in range(len(matrix))]