import sys
from diGraphExample import diGraphExample
from graphExample import graphExample
from edgeWeightedGraph import edgeWeightedGraph
from shortestPath import dijkstraPathExample
from negativeCycle import negativeCycle
from currencyArbitrage import currencyArbitrage

if len(sys.argv) < 2:
    raise "Please provide arguments"

if (sys.argv[1] == "ug"):
    graphExample()
elif (sys.argv[1] == "dig"):
    diGraphExample()
elif (sys.argv[1] == "ewg"):
    edgeWeightedGraph()
elif (sys.argv[1] == "dij"):
    dijkstraPathExample()
elif (sys.argv[1] == "nc"):
    negativeCycle()
elif (sys.argv[1] == "ca"):
    currencyArbitrage()
else:
    raise "Please provide valid argument!"
