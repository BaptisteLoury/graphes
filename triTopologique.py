import implement as imp

# deprecated
def get_vertex_without_predecessor(matrix):
    with_predecessor = []
    for vertex in range(len(matrix)):
        for predecessor in range(len(matrix[vertex])):
            a = matrix[vertex][predecessor]
            if a != 0 and predecessor not in with_predecessor:
                with_predecessor.append(predecessor)

    return [vertex for vertex in range(len(matrix[0])) if vertex not in with_predecessor]

# expect list of tuple(int,list(int)) that stands for tuple(vertex,predecessors)
def get_vertex_without_predecessor_V2(matrix):
    with_predecessor = []
    for vertex in matrix:
        for prede in range(len(vertex[1])):
            if vertex[1][prede] != 0 and prede not in with_predecessor:
                with_predecessor.append(prede)

    return [vertex[0] for vertex in matrix if vertex[0] not in with_predecessor]

def remove_vertex_from_matrix(matrix,vertexes):
    for vertex in matrix:
        for xetrev in vertexes:
            if vertex[0] == xetrev:
                matrix.remove(vertex)

def topology_sorting(matrix):
    transition_matrix = imp.matrix_with_index(matrix)
    sort = []
    N = 1
    Y = [vertex for vertex in range(len(matrix))]
    while Y:
        without_predecessor = get_vertex_without_predecessor_V2(transition_matrix)
        remove_vertex_from_matrix(transition_matrix,without_predecessor)
        Y = [vertex for vertex in Y if vertex not in without_predecessor]
        sort.append((N,without_predecessor))
        N += 1
    return sort

def beautiful_topo_sort(sort):
    for N in sort:
        print(N[0],":",N[1])