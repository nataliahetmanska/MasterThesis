import networkx as nx
import matplotlib
import numpy as np

watts_strogatz = nx.watts_strogatz_graph(100,30,0.15)
print(nx.number_of_edges(watts_strogatz))