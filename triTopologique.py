import implement as imp

def get_vertex_without_predecessor(matrix,already_sorted):
    without_predecessor = []

    # pour chaque sommet du graphe
    for som in range(len(matrix)):
        has_predecessor = False
        pred = 0

        # tant que le sommet n'a pas de prédecesseur
        while(not has_predecessor and pred < len(matrix)):
            # on parcourt la matrice en colonne (prédécesseurs) et non en ligne (successeurs)
            # si la case pred;som est différente de 0 alors pred est prédecesseur de som
            has_predecessor = matrix[pred][som] > 0
            pred += 1

        # si le sommet n'a pas de prédecesseur
        if not has_predecessor and som not in already_sorted:
            # on l'ajoute
            without_predecessor.append(som)
    
    return without_predecessor

def remove_vertex_from_matrix(matrix,vertexes):
    # pour chaque sommet de vertexes
    for vertex in vertexes:
        # pour chacun de ses successeurs
        for succ in range(len(matrix)):
            # on supprime la liaison sommet*successeur
            matrix[vertex][succ] = 0

def topology_sorting(matrix):
    # on copie matrix dans une nouvelle instance
    transition_matrix = [[i for i in k] for k in matrix]
    sort = []

    # on initialise le niveau à 1
    N = 1

    # on place dans Y tous les sommets de matrix
    Y = [vertex for vertex in range(len(matrix))]

    already_sorted = []

    # tant qu'il reste des sommets non triés (Y non vide)
    while Y:
        # on récupère les sommets sans prédécesseurs
        without_predecessor = get_vertex_without_predecessor(transition_matrix,already_sorted)

        # on enlève les sommets sans prédécesseurs de la matrice de transition
        remove_vertex_from_matrix(transition_matrix,without_predecessor)

        # on enlève les sommets sans prédécesseurs de Y
        Y = [vertex for vertex in Y if vertex not in without_predecessor]

        # on ajoute le rang actuel et la liste des sommets associés
        sort.append((N,without_predecessor))

        # on ajoute les sommets sans prédécesseurs à ceux déjà triés
        already_sorted.extend(without_predecessor)

        # on passe au rang suivant
        N += 1

    return sort

def beautiful_topo_sort(sort):
    for N in sort:
        print(N[0],":",N[1])