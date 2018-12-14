import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def diGraphExample(fileName="diGraph.png"):
    print()
    G = nx.DiGraph()
    G.add_nodes_from(range(0, 6))
    G.add_edges_from({
        (0, 1),
        (0, 2),
        (0, 5),
        (1, 4),
        (3, 2),
        (3, 5),
        (3, 4),
        (3, 6),
        (5, 2),
        (6, 0),
        (6, 4),
    })
    print(list(G.nodes))
    print(list(G.edges))

    if nx.is_directed_acyclic_graph(G):
        print('DAG constructed. Printing topological sort: ')
        print(list(nx.topological_sort(G)))
    else:
        raise("NOT a DAG")

    nx.draw(G, pos=nx.spring_layout(G), with_labels=True, font_weight='bold')
    print("Saving file to " + str(fileName))
    plt.savefig(fileName)
    print()
