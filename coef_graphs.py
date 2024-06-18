import pandas as pd
import networkx as nx
import pickle
import numpy as np


def create_real_graph(file_name):
    graph = nx.Graph()
    edges = pd.read_csv(file_name, names=["Start", "End"])

    start = edges["Start"].tolist()
    end = edges["End"].tolist()

    for i in range(len(start)):
        graph.add_edge(start[i], end[i])

    return graph


def generate_ws_graph(n, k, p):
    G = nx.watts_strogatz_graph(n, k, p)
    clustering_coeff = nx.average_clustering(G)
    avg_degree = np.mean([d for _, d in G.degree()])
    avg_shortest_path = nx.average_shortest_path_length(G)
    return G, clustering_coeff, avg_degree, avg_shortest_path


files = ["S1Anonymized.csv", "S2Anonymized.csv", "M1Anonymized.csv", "M2Anonymized.csv", "L1Anonymized.csv",
         "L2Anonymized.csv"]

clustering_list = []
degree_list = []
avg_degree_list = []
avg_shortest_pth_list = []

for file in files:
    G = create_real_graph(file)
    pickle.dump(G, open(f'graph{file}.pickle', 'wb'))
    clustering_list.append(nx.clustering(G))
    degree_list.append(nx.degree(G))
    avg_degree_list.append(np.mean([d for _, d in G.degree()]))
    avg_shortest_pth_list.append(nx.average_shortest_path_length(G))

    target_degree = np.mean([d for _, d in G.degree()])
    target_clustering = nx.average_clustering(G)

    # Initial guess for p
    p = 0.1
    k = int(round(target_degree))
    N = G.number_of_nodes()

    graph, clustering_coeff, avg_degree, avg_shortest_path = generate_ws_graph(N, k, p)

    while abs(clustering_coeff - target_clustering) > 0.01:
        if clustering_coeff > target_clustering:
            p += 0.01
        else:
            p -= 0.01
        graph, clustering_coeff, avg_degree, avg_shortest_path = generate_ws_graph(N, k, p)

    pickle.dump(graph, open(f'graph{file}_WS.pickle', 'wb'))
