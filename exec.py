import implement as imp

# graphe = [[1,2], [2], [3], [4], []]
# graphe=[[0,2,3,4],[1,2,4],[0,2,3,4],[1,2,3,4],[0,2,4]]
# graphe=[[4,6,8,9],[1,2,7,9],[0,2,9],[1,4,5,6,8,9],[1,8,9],[3,4,6,9],[2,3,5,6,8,9],[3,4,5,6,8,9],[0,1,3,6,8,9],[0,1,2,5,7,9]]
graphe=[[0,1,2,6,7,9],[1,8,9],[1,3,5,8,9],[0,2,3,4,6,9],[1,3,4,7,9],[1,4,9],[4,6,7,9],[1,2,5,9],[0,3,5,6,9],[2,5,9]]



# Séance 1
matrix = imp.calc_matrice_adj(graphe)
print("Matrice d'adjacence")
imp.var_dump_table(matrix)
print("Matrice de Roy Warshall (matrice)")
matrix = imp.roy_warshall_for_matrice(matrix)
imp.var_dump_table(matrix)
# print("Matrice de Roy Warshall (list of list)")
# graphe = roy_warshall_for_list_of_list(graphe)
# var_dump_table(graphe)