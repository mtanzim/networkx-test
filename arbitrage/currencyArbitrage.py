import networkx as nx
import bellmanford as bf
import pydot
from constants import SUBDIRNAME, ROUNDING_DIGITS, STARTVAL, BASECUR
from decimal import Decimal
import json
import numpy as np

import requests


def callAPI():
    print('API DATA')
    url = "https://fx.priceonomics.com/v1/rates/?q=1"
    r = requests.get(url)
    jsonData = r.json()
    for key in jsonData:
        print(key+'\t'+str(jsonData[key]))
    print()

    return jsonData


def getCurData(jsonData, isLn):

    print()
    if (isLn):
        print('Building Ln Graph Edges')
    else:
        print('Building Graph Edges')

    edge_data = []
    for key in jsonData:
        if (key.split('_')[0] != key.split('_')[1]):
            val = float(jsonData[key])
            if (isLn):
                lnVal = Decimal(np.log(val) * -1)
                edge_data.append(
                    (key.split('_')[0], key.split('_')[1], lnVal))
            else:
                edge_data.append(
                    (key.split('_')[0], key.split('_')[1], Decimal(val)))

    return edge_data


def plotGraphs(Gprime, cyclicEdgeList, fileName):
    # plot graphs
    # modify G to include labels for weights, and color coding for cyclic edges so it can be drawn
    for edge in Gprime.edges():

        # round the edge values
        Gprime[edge[0]][edge[1]][0].update(
            {'weight': round(Gprime[edge[0]][edge[1]][0]['weight'], ROUNDING_DIGITS)})

        # add labels
        Gprime[edge[0]][edge[1]][0].update(
            {'label': Gprime[edge[0]][edge[1]][0]['weight']})

        # highlight circular edges
        if edge in cyclicEdgeList:
            Gprime[edge[0]][edge[1]][0].update(
                {'color': 'red'})

    # convert to dot
    d = nx.drawing.nx_pydot.to_pydot(Gprime)
    print("Visualizing graph to " + str(fileName))
    d.write_png(fileName)


def currencyArbitrage(edgeData, fileName, checkCycle):

    G = nx.MultiDiGraph()
    G.add_weighted_edges_from(edgeData)

    length, nodes, negative_cycle = bf.negative_edge_cycle(G, weight='weight')
    cyclicEdgeList = []
    cyclicEdgeListStr = []
    if (negative_cycle and checkCycle):
        print('Checking negative cycles')
        cycleWeight = Decimal(0)
        print('Negative cycles found!')
        for i in range(1, len(nodes)):
            curNode = nodes[i]
            prevNode = nodes[i-1]
            cyclicEdgeList.append((prevNode, curNode))
            cyclicEdgeListStr.append(prevNode+'_'+curNode)
            cycleWeight = cycleWeight + \
                Decimal(G[prevNode][curNode][0]['weight'])
            print(str(prevNode) + ' -> ' + str(curNode))

    plotGraphs(G.copy(), cyclicEdgeList, fileName)

    # return cyclic edge list and starting currency
    if checkCycle and negative_cycle:
        return nodes[0], cyclicEdgeListStr


def main():

    print()
    jsonData = callAPI()
    currencyArbitrage(getCurData(jsonData, False),
                      "./"+SUBDIRNAME+"/curArb.png", False)

    startCur, cyclicEdgeList = currencyArbitrage(getCurData(jsonData, True),
                                                 "./"+SUBDIRNAME+"/curArbLn.png", True)

    startVal = Decimal(STARTVAL)
    newVal = startVal
    for edge in cyclicEdgeList:
        newVal = Decimal(newVal*Decimal(float(jsonData[edge])))
    profit = newVal - startVal
    profitBaseCur = Decimal(
        profit*Decimal(float(jsonData[startCur+'_'+BASECUR])))

    print()
    # print('Results')
    print('Starting conversions with below arbitrage cycle:')
    print(cyclicEdgeList)
    print()

    print('Starting Value in: '+startCur)
    print(round(startVal, ROUNDING_DIGITS))
    print('Ending Value in: '+startCur)
    print(round(newVal, ROUNDING_DIGITS))
    print('Profit in: '+startCur)
    print(round(newVal - startVal, ROUNDING_DIGITS))

    print()
    print('Starting Value in: '+BASECUR)
    print(round(profit, ROUNDING_DIGITS))
    print('Profit in: '+BASECUR)
    print(round(profitBaseCur, ROUNDING_DIGITS))
    print()
