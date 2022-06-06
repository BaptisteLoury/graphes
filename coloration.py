import implement as imp
import draw_graphs as draw

def cnt_tuple(e):
    return e[1]

def sommets_par_degres_decroissant(graphe):
    # pour chaque sommet on l'associe à un degré (0 par défaut)
    sommets = [(som,0) for som in range(len(graphe))]

    # pour chaque sommet
    for som in range(len(graphe)):
        # pour chacun de ses successeurs
        for succ in graphe[som]:
            # on augmente le degré du sommet
            sommets[som] = (sommets[som][0],sommets[som][1] + 1)
            # et le degré du succeseur
            sommets[succ] = (sommets[succ][0],sommets[succ][1] + 1)
            # cela nous permet de gérer les graphes orientés ET non orientés

    # on tri en fonction du degré décroissant
    sommets.sort(key=cnt_tuple, reverse=True)

    # on retourne unique le sommet (le degré ne sert à rien)
    return [elem[0] for elem in sommets]
      

def get_voisins(som,graphe):
    # on ajoute aux voisins tous les successeurs du sommet
    voisins = [s for s in graphe[som]]
    # pour chaque sommet
    for s in range(len(graphe)):
        # pour chacun de ses successeurs
        for succ in graphe[s]:
            # si le successeur est le sommet
            if succ == som and s not in voisins:
                # on ajoute le voisin
                voisins.append(s)
    return voisins


def has_voisin_select(som,selection,graphe):
    has_voisin = False

    # pour chaque voisib
    for v in get_voisins(som,graphe):
        # si le voisin est sélectionné
        if v in selection:
            # alors som a un voisin
            has_voisin = True

    return has_voisin


def welsh_powell(graphe):
    # récupération des sommets par degré décroissant
    sommets = sommets_par_degres_decroissant(graphe)

    color_group = []

    # tant qu'il reste des sommets à grouper
    while sommets != []:
        selection = []
        # pour chaque sommet restant dans sommets
        for som in sommets:
            # si le sommet n'a pas de voisin déjà selectionné
            if not has_voisin_select(som,selection,graphe):
                # on sélectionne le sommet
                selection.append(som)

        # on ajoute tous les sommets selectionnées aux groupes de couleur
        color_group.append(selection)

        # n enlève les sommets selectionnés de sommets
        sommets = [som for som in sommets if som not in selection]

    # on a color_group sous la forme :
    # [ [0,4,5], [1,2], [3] ] où 0,4 et 5 ont la même couleur, 1 et 2 une autre, et 3 le seul de sa couleur
    # graph_color_map va associer tous les sommets d'un groupe à une même couleur et retourne :
    # ['blue', 'green', 'green', 'red', 'blue', 'blue']
    return draw.graph_color_map(color_group)