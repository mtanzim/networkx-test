import sys
from diGraphExample import diGraphExample
from graphExample import graphExample
from edgeWeightedGraph import edgeWeightedGraph
from shortestPath import dijkstraPathExample
from negativeCycle import negativeCycle

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
else:
    raise "Please valid provide argument!"
