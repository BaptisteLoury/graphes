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

def matrix_with_index(matrix):
    return [(i,matrix[i]) for i in range(len(matrix))]