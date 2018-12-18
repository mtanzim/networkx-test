import networkx as nx
import pydot
from constants import SUBDIRNAME


def negativeCycle(fileName="./"+SUBDIRNAME+"/negCycle.png"):
    print()
    G = nx.MultiDiGraph()
    G.add_edges_from([
        (4, 5, {'weight': 0.35}),
        (5, 4, {'weight': -0.66}),
        (4, 7, {'weight': 0.37}),
        (5, 7, {'weight': 0.28}),
        (7, 5, {'weight': 0.28}),
        (5, 1, {'weight': 0.32}),
        (0, 4, {'weight': 0.38}),
        (0, 2, {'weight': 0.26}),
        (7, 3, {'weight': 0.39}),
        (1, 3, {'weight': 0.29}),
        (2, 7, {'weight': 0.34}),
        (6, 2, {'weight': 0.40}),
        (3, 6, {'weight': 0.52}),
        (6, 0, {'weight': 0.58}),
        (6, 4, {'weight': 0.93}),
    ])

    print('Negative cycles: ' + str(nx.negative_edge_cycle(G)))

    Gprime = G.copy()
    # modify G to include labels for weights, so it can be drawn
    for edge in G.edges():
        Gprime[edge[0]][edge[1]][0].update(
            {'label': Gprime[edge[0]][edge[1]][0]['weight']})

    # convert to dot
    d = nx.drawing.nx_pydot.to_pydot(Gprime)
    print(d)
    print("Saving file to " + str(fileName))
    d.write_png(fileName)
