from constants import SUBDIRNAME
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
matplotlib.use('agg')


def dijkstraPathExample(fileName="./"+SUBDIRNAME+"/dijkstraSP.png"):
    print()
    G = nx.DiGraph()
    G.add_weighted_edges_from([
        (0, 1, 5.0),
        (0, 4, 9.0),
        (0, 7, 8.0),
        (1, 2, 12.0),
        (1, 3, 15.0),
        (1, 7, 4.0),
        (2, 3, 3.0),
        (2, 6, 11.0),
        (3, 6, 9.0),
        (4, 5, 4.0),
        (4, 6, 20.0),
        (4, 7, 5.0),
        (5, 2, 1.0),
        (5, 6, 13.0),
        (7, 5, 6.0),
        (7, 2, 7.0),
    ])

    sourceNode = 0
    sp = nx.single_source_dijkstra_path(G, sourceNode)
    spL = nx.single_source_dijkstra_path_length(G, sourceNode)

    finalEdgeTo = {}

    print('Shortest paths and weights')
    print('Node\tedgeTo\tWeight')
    for node in sorted(sp):
        # if (node != sourceNode):
        print(str(node) + '\t' + str(sp[node]) + '\t\t' + str(spL[node]))
        if (node != sourceNode):
            finalEdgeTo[(sp[node][-2], sp[node][-1])
                        ] = {"sp"+str(sourceNode): 'sp'+str(sourceNode)}
            # print (str(node) + '\t' + str((sp[node][-2], sp[node][-1]))+'\t'+str(spL[node]))

    nx.set_edge_attributes(G, finalEdgeTo)
    print('updated graph')
    print(G.edges.data())

    labels = nx.get_edge_attributes(G, 'sp0')
    pos = nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    print("Saving file to " + str(fileName))
    plt.savefig(fileName)
    print()
