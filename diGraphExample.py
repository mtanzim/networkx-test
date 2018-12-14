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
        (4, 2),
        (2, 4),
        (0, 5),
        (1, 4),
        (4, 1),
        (3, 2),
        (3, 5),
        (3, 4),
        (3, 6),
        (5, 2),
        (6, 0),
        (0, 6),
        (6, 4),
    })
    print('Nodes')
    print(list(G.nodes))
    print('Edges')
    print(list(G.edges))

    print('DFS nodes from 0')
    print(list(nx.dfs_postorder_nodes(G,0)))

    print('Printing shortest paths from 0')
    for i in range(1, 6):
        try:
            print(list(nx.shortest_path(G, 0, i)))
        except:
            print('No path for node: ' + str(i)) 


    if nx.is_directed_acyclic_graph(G):
        print('DAG constructed. Printing topological sort: ')
        print(list(nx.topological_sort(G)))
    else:
        print("NOT a DAG")


    print('Strongly connected components')
    print(list(nx.strongly_connected_components(G)))
    

    nx.draw(G, pos=nx.circular_layout(G), with_labels=True, font_weight='bold')
    print("Saving file to " + str(fileName))
    plt.savefig(fileName)
    print()
