import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from networkx.algorithms import tree
from constants import SUBDIRNAME


def edgeWeightedGraph(fileName="./"+SUBDIRNAME+"/ewg.png"):
  print()
  G = nx.Graph()
  G.add_weighted_edges_from([
    (0,7,0.16),
    (2,3,0.17),
    (1,7,0.19),
    (0,2,0.26),
    (5,7,0.28),
    (1,3,0.29),
    (1,5,0.32),
    (2,7,0.34),
    (4,5,0.35),
    (1,2,0.36),
    (4,7,0.37),
    (0,4,0.38),
    (6,2,0.40),
    (3,6,0.52),
    (6,0,0.58),
    (6,4,0.93),
  ])

  # print(list(G.nodes))

  print ('Minimum Spanning Tree')
  # mst = tree.minimum_spanning_edges(G, algorithm='kruskal', data=False)
  mst = tree.minimum_spanning_edges(G, algorithm='prim', data=False)
  edgelist = list(mst)
  edgeAttr = nx.get_edge_attributes(G, 'weight')

  # T = nx.minimum_spanning_tree(G)
  # print (sorted(T.edges(data=True)))

  mstWeight = 0
  print ('Edge Weight List')
  for edge in edgelist:
    mstWeight += float(edgeAttr[edge])
    print(str(list(edge)) + '\t' + str(edgeAttr[edge]))

  print ('Total MST Weight: ' + str(mstWeight))

  # print(sorted(edgelist))
  # print('List of edges')

  labels = nx.get_edge_attributes(G,'weight')
  pos = nx.circular_layout(G)
  nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
  nx.draw(G, pos, with_labels=True, font_weight='bold')
  print("Saving file to " + str(fileName))
  plt.savefig(fileName)
  print()
