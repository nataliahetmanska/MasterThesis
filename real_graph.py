import pandas as pd
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt






G = create_real_graph("M1Anonymized", graph)
pos = nx.circular_layout(G)
nx.draw(G, pos=pos)
plt.savefig("real_network.png")