import networkx as nx
import matplotlib.pyplot as plt

colors = ['red','blue','green','gray','orange','purple','yellow']

def draw_graph_from_matrix(matrix):
    G = nx.Graph()
    
    for row in range(len(matrix)):
        for col in range(row + 1):
            if matrix[row][col] != 0:
                G.add_edge(col,row,weight=matrix[row][col])

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, font_weight='bold')

    nx.draw_networkx_edge_labels(G, pos, edge_labels={edge:G.edges[edge]['weight'] for edge in G.edges})

def draw_graphs_from_matrixes(m1,m2):
    G1 = nx.Graph()
    G2 = nx.Graph()
    
    for row in range(len(m1)):
        for col in range(row + 1):
            if m1[row][col] != 0:
                G1.add_edge(col,row,weight=m1[row][col])

    for row in range(len(m2)):
        for col in range(row + 1):
            if m2[row][col] != 0:
                G2.add_edge(col,row,weight=m2[row][col])

    subax1 = plt.subplot(121)

    pos = nx.spring_layout(G1)

    nx.draw(G1, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G1, pos, edge_labels={edge:G1.edges[edge]['weight'] for edge in G1.edges})

    subax2 = plt.subplot(122)

    pos = nx.spring_layout(G2)

    nx.draw_shell(G2, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G2, pos, edge_labels={edge:G2.edges[edge]['weight'] for edge in G2.edges})

    plt.show()

def draw_graph(graph,color_map):
    G = nx.DiGraph()

    for som in range(len(graph)):
        G.add_node(som)

    for som in range(len(graph)):
        for succ in range(len(graph[som])):
            if graph[som][succ] != 0:
                G.add_edge(som,succ)


    nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')

    plt.show()

def graph_color_map(color_group):
    cardinal = 0
    for gr in color_group:
        cardinal += len(gr)

    color_map = ['black' for i in range(cardinal)]

    for gr in range(len(color_group)):
        for som in color_group[gr]:
            color_map[som] = colors[gr]

    return color_map