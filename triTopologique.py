import implement as imp

# expect list of tuple(int,list(int)) that stands for tuple(vertex,predecessors)
def get_vertex_without_predecessor(matrix,already_sorted):
    without_predecessor = []
    for som in range(len(matrix)):
        has_predecessor = False
        pred = 0
        while(not has_predecessor and pred < len(matrix)):
            has_predecessor = matrix[pred][som] > 0
            pred += 1

        if not has_predecessor and som not in already_sorted:
            without_predecessor.append(som)
    
    return without_predecessor

def remove_vertex_from_matrix(matrix,vertexes):
    for vertex in vertexes:
        for succ in range(len(matrix)):
            matrix[vertex][succ] = 0

def topology_sorting(matrix):
    transition_matrix = [[i for i in k] for k in matrix]
    sort = []
    N = 1
    Y = [vertex for vertex in range(len(matrix))]
    already_sorted = []
    while Y:
        without_predecessor = get_vertex_without_predecessor(transition_matrix,already_sorted)
        remove_vertex_from_matrix(transition_matrix,without_predecessor)
        Y = [vertex for vertex in Y if vertex not in without_predecessor]

        sort.append((N,without_predecessor))
        already_sorted.extend(without_predecessor)
        N += 1

    return sort

def beautiful_topo_sort(sort):
    for N in sort:
        print(N[0],":",N[1])