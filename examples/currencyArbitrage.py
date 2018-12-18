import networkx as nx
import bellmanford as bf
import pydot
from constants import SUBDIRNAME
from decimal import Decimal
import json
import numpy as np

import requests


def getCurData():
    url = "https://fx.priceonomics.com/v1/rates/?q=1"
    r = requests.get(url)
    json_data = r.json()

    edge_data = []

    for key in json_data:
        # print(key)
        # print(json_data[key])
        if (key.split('_')[0] != key.split('_')[1]):

            val = float(json_data[key])
            lnVal = np.log(val) * -1
            lnRounded = round(Decimal(lnVal), 5)

            edge_data.append((key.split('_')[0], key.split('_')[1], lnRounded))
    return edge_data


def currencyArbitrage(fileName="./"+SUBDIRNAME+"/curArb.png"):

    getCurData()
    print()
    G = nx.MultiDiGraph()
    G.add_weighted_edges_from(getCurData())

    print(bf.negative_edge_cycle(G, weight='weight'))
    length, nodes, negative_cycle = bf.negative_edge_cycle(G, weight='weight')
    cyclicEdgeList = []
    if (negative_cycle == True):
        for i in range(1, len(nodes)):
            cyclicEdgeList.append((nodes[i-1], nodes[i]))
        print(cyclicEdgeList)

    Gprime = G.copy()
    # modify G to include labels for weights, so it can be drawn
    for edge in Gprime.edges():
        if edge in cyclicEdgeList:
            print('This is a cyclic edge')
            print(edge)
            Gprime[edge[0]][edge[1]][0].update(
                {'color': 'red'})

        Gprime[edge[0]][edge[1]][0].update(
            {'label': Gprime[edge[0]][edge[1]][0]['weight']})

    # convert to dot
    d = nx.drawing.nx_pydot.to_pydot(Gprime)
    print(d)
    print("Saving file to " + str(fileName))
    d.write_png(fileName)
