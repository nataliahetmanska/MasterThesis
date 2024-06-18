import networkx as nx
import matplotlib.pyplot as plt

N = 20
beta = 0.3
k = 5

'''G = nx.watts_strogatz_graph(N, k, beta)
pos = nx.circular_layout(G)
nx.draw(G, pos=pos)
plt.savefig("ws_graph.png")'''

G= nx.complete_graph(N)
pos = nx.circular_layout(G)
nx.draw(G, pos=pos)
plt.savefig("com_graph.png")