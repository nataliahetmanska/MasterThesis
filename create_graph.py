import networkx as nx
import pickle

N = 1000
beta = 0.3
k = [30, 50, 80, 120]

def create_graph(N, k, beta):

   graph = nx.watts_strogatz_graph(N, k, beta)

   return graph

for amt in k:
   graph = create_graph(N, amt, beta)
   pickle.dump(graph, open(f'graph{amt}.pickle', 'wb'))

