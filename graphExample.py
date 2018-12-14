import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


def graphExample(fileName="simpleGraph.png"):
    print()
    G = nx.Graph()

    G.add_nodes_from(range(0, 12))
    G.add_edges_from({
        (0, 1),
        (0, 2),
        (0, 6),
        (0, 5),
        (5, 3),
        (4, 3),
        (5, 4),
        (6, 4),
        (7, 8),
        (9, 10),
        (9, 11),
        (9, 12),
    })

    # print(list(G.nodes))
    # print(list(G.edges))
    # print (list(nx.dfs_preorder_nodes(G, 0)))
    # print (list(nx.bfs_tree(G, 0).edges()));
    print('Connected components')
    print(list(nx.connected_components(G)))

    print('Printing shortest paths from 0`')
    for i in range(1, 12):
        try:
            print(list(nx.shortest_path(G, 0, i)))
        except:
            print('No path for node: ' + str(i))

    nx.draw(G, pos=nx.circular_layout(G), with_labels=True, font_weight='bold')
    print("Saving file to " + str(fileName))
    plt.savefig(fileName)
    print()
