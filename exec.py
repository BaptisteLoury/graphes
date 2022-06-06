import implement as imp
import triTopologique as tp
import draw_graphs as draw
import coloration as colo
import arbre_couvrant_pds_min as abr

# network x pour afficher les graphes

#graphe = [[1,2], [2], [3], [4], []]
# graphe = [[1,2], [2], [3], [4], []]
# graphe=[[0,2,3,4],[1,2,4],[0,2,3,4],[1,2,3,4],[0,2,4]]
graphe=[[4,6,8,9],[1,2,7,9],[0,2,9],[1,4,5,6,8,9],[1,8,9],[3,4,6,9],[2,3,5,6,8,9],[3,4,5,6,8,9],[0,1,3,6,8,9],[0,1,2,5,7,9]]
# graphe=[[0,1,2,6,7,9],[1,8,9],[1,3,5,8,9],[0,2,3,4,6,9],[1,3,4,7,9],[1,4,9],[4,6,7,9],[1,2,5,9],[0,3,5,6,9],[2,5,9]]
# graphe = [[1,3], [4], [4,5], [], [3], []]
# graphe = [[1,3], [2,5], [], [4],[], [6],[]]
# graphe=[[1,3],[2,],[0,3],[5],[3],[4]]

# Debut séance 1
graphe1=[[0,2,3,4],[1,2,4],[0,2,3,4],[1,2,3,4],[0,2,4]]
graphe2=[[4,6,8,9],[1,2,7,9],[0,2,9],[1,4,5,6,8,9],[1,8,9],[3,4,6,9],[2,3,5,6,8,9],[3,4,5,6,8,9],[0,1,3,6,8,9],[0,1,2,5,7,9]]
graphe3=[[0,1,2,6,7,9],[1,8,9],[1,3,5,8,9],[0,2,3,4,6,9],[1,3,4,7,9],[1,4,9],[4,6,7,9],[1,2,5,9],[0,3,5,6,9],[2,5,9]]

matrice1=imp.calc_matrice_adj(graphe1)
matrice2=imp.calc_matrice_adj(graphe2)
matrice3=imp.calc_matrice_adj(graphe3)

print(imp.roy_warshall_for_matrice(matrice1))
# print(imp.roy_warshall_for_matrice(matrice2))
# print(imp.roy_warshall_for_matrice(matrice3))




# print("le graphe de départ est ")
# print(graphe)
# def print_seance1():
    # Séance 1
# matrix = imp.calc_matrice_adj(graphe)
# print("Matrice d'adjacence")
# print(matrix)

# graphe = [[1,3], [4], [4,5], [], [3], []]
# graphe = [[1,2], [2], [3,5], [4], [], [4]]
# graphe = [[3,5,7],[2,4,6],[5,7,1],[0,4,6],[7,3,1],[0,2,6],[1,3,5],[0,2,4]]
# graphe = [[1,2], [2], [3], []]

matrice2=imp.matrice_predecesseur(graphe)
# print(matrice2)
    # imp.var_dump_table(matrix)
    # print("Matrice de Roy Warshall (matrice)")
    # matrix = imp.roy_warshall_for_matrice(matrix)
    # imp.var_dump_table(matrix)
    # print("Matrice de Roy Warshall (list of list)")
    # graphe = roy_warshall_for_list_of_list(graphe)
    # var_dump_table(graphe)
    
# parcouru=imp.parcourir_graphe_profondeur(graphe,1)
# print(parcouru)


# composantes_connexes=imp.determiner_composantes_connexes(graphe)
# print(composantes_connexes)

# def print_seance2():
#     matrix = imp.calc_matrice_adj(graphe)s
#     print("Matrice d'adjacence")
#     imp.var_dump_table(matrix)
#     topo_sorting = tp.topology_sorting(matrix)
#     print("Tri topologique")
#     tp.beautiful_topo_sort(topo_sorting)

# print_seance1()

def print_seance3():
    color_map = draw.graph_color_map(colo.welsh_powell(graphe))
    draw.draw_graph(graphe,color_map)

def print_seance4():
    matrix = imp.calc_matrice_adj_non_orient(graphe)
    matrix_ponderee = imp.ponderation_graphe_non_orient(imp.calc_matrice_adj_non_orient(graphe))
    draw.draw_graphs_from_matrixes(matrix_ponderee,abr.kruskal(matrix_ponderee))
    # draw.draw_graphs_from_matrixes(matrix,matrix)


print_seance4()
