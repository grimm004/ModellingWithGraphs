import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    visited = [v for v in G.nodes() if G.node[v]['visited'] == 'yes']
    for v in G.nodes():
        if v in visited:
            continue
        for u in visited:
            if v in G[u]:
                return v
    return 1


def find_smallest_color(G,i):
    node_colour = 1
    node_colours = [G.node[neighbour]['color'] for neighbour in sorted(G[i]) if G.node[neighbour]['color'] != 0]
    while node_colour in node_colours:
        node_colour += 1
    return node_colour


def greedy(G):
    global kmax
    global visited_counter
    visited_counter = 0
    n = len(G.nodes())

    while visited_counter < n:
        i = find_next_vertex(G)
        G.node[i]['color'] = find_smallest_color(G, i)
        G.node[i]['visited'] = 'yes'
        visited_counter += 1

    kmax = max(G.node[v]['color'] for v in G.nodes())

    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
