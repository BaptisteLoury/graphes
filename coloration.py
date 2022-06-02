import implement as imp

def cnt_tuple(e):
    return e[1]

def sommets_par_degres_croissant(graphe):
    sommets = [(som,0) for som in range(len(graphe))]
    for som in range(len(graphe)):
        for succ in graphe[som]:
            sommets[som] = (sommets[som][0],sommets[som][1] + 1)
            sommets[succ] = (sommets[succ][0],sommets[succ][1] + 1)

    sommets.sort(key=cnt_tuple, reverse=True)

    return [elem[0] for elem in sommets]
      

def get_voisins(som,graphe):
    voisins = [s for s in graphe[som]]
    for s in range(len(graphe)):
        for succ in graphe[s]:
            if succ == som and s not in voisins:
                voisins.append(s)
    return voisins


def has_voisin_select(som,selection,graphe):
    has_voisin = False
    for v in get_voisins(som,graphe):
        if v in selection:
            has_voisin = True 
    return has_voisin


def welsh_powell(graphe):
    sommets = sommets_par_degres_croissant(graphe)

    color_group = []

    while sommets != []:
        selection = []
        for som in sommets:
            if not has_voisin_select(som,selection,graphe):
                selection.append(som)

        color_group.append(selection)

        sommets = [som for som in sommets if som not in selection]

    return color_group