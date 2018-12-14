import sys
from diGraphExample import diGraphExample
from graphExample import graphExample

if len(sys.argv) < 2:
    raise "Please provide arguments"

if (sys.argv[1] == "ug"):
    graphExample()
elif (sys.argv[1] == "dig"):
    diGraphExample()
else:
    raise "Please valid provide argument!"
