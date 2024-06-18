import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import pandas as pd
import networkx as nx
 # number of agents
msc_all = 500 # number of Monte Carlo steps
q_a = 8  # number of agents we choose if chosen agent is anticonformist
q_c = 2  # number of agents we choose if chosen agent is conformist

p = 0.2 # propability that the agent is always anticonformist
c = 0.1  # initial concentration of agents with a positive opinion

beta = 0.3 #The probability of rewiring each edge
k = [30, 50, 80, 120] #k nearest neighbors

'''def create_real_graph(file_name):
    graph = nx.Graph()
    edges = pd.read_csv(file_name, names= ["Start", "End"])

    start = edges["Start"].tolist()
    end = edges["End"].tolist()

    for i in range(len(start)):
        graph.add_edge(start[i], end[i])

    return graph
'''
def initial_opinions(c, N):
   opinions = list()
   for i in range(N):
       r_i = rnd.uniform(0, 1)
       if r_i < c:
           opinions.append(1)
       else:
           opinions.append(-1)

   return opinions

def initial_behaviours(p, N):
   behaviours = list()

   for i in range(N):
       h_i = rnd.uniform(0, 1)
       if h_i < p:
           behaviours.append(-1)
       else:
           behaviours.append(1)

   return behaviours


def opinions(N):

    #G = pickle.load(open(f'graph{file}.pickle', 'rb'))

    G = nx.complete_graph(N)

    N = G.number_of_nodes()

    opinions = initial_opinions(c, N)
    behaviours = initial_behaviours(p, N)

    time = 0
    ones_total = list()
    minus_total = list()

    while time <= msc_all:

        ones = list()
        minus = list()

        for t in range(N):

           i = rnd.randint(1, N-1)


           rnd_agent_bh = behaviours[i]
           neighbours = list(G.neighbors(i))

           if rnd_agent_bh == -1:

               rnd_neigh = rnd.sample(neighbours, min(q_a, len(neighbours)))

               neigh_ops = list()

               for l in range(len(rnd_neigh)):
                   if rnd_neigh[l] < len(opinions):
                       neigh_ops.append(opinions[rnd_neigh[l]])

               if len(set(neigh_ops)) == 1:

                    if neigh_ops[0] == 1:
                        opinions[i] = -1

                    elif neigh_ops[0] == -1:
                        opinions[i] = 1

                    count_ones = opinions.count(1)
                    count_minus_ones = opinions.count(-1)

                    ones.append(count_ones)
                    minus.append(count_minus_ones)

               else:
                    count_ones = opinions.count(1)
                    count_minus_ones = opinions.count(-1)

                    ones.append(count_ones)
                    minus.append(count_minus_ones)

           if rnd_agent_bh == 1:

               rnd_neigh = rnd.sample(neighbours,  min(q_c, len(neighbours)))
               neigh_ops = list()

               for l in range(len(rnd_neigh)):

                   if rnd_neigh[l] < len(opinions):
                       neigh_ops.append(opinions[rnd_neigh[l]])

               if len(set(neigh_ops)) == 1:
                    if neigh_ops[0] == 1:
                        opinions[i] = 1
                    else:
                        opinions[i] = -1
                    count_ones = opinions.count(1)
                    count_minus_ones = opinions.count(-1)

                    ones.append(count_ones)
                    minus.append(count_minus_ones)

               else:
                    count_ones = opinions.count(1)
                    count_minus_ones = opinions.count(-1)

                    ones.append(count_ones)
                    minus.append(count_minus_ones)

        ones_total.append(np.mean(ones))
        minus_total.append(np.mean(minus))
        time = time +1


    times = list(range(1, len(ones_total)+1))
    positive_conc = list()

    for i in ones_total:
       positive_conc.append(i/N)

    negative_conc = list()

    for i in minus_total:
       negative_conc.append(i/N)

    plt.figure(figsize=(10, 8))
    plt.plot(times, positive_conc, negative_conc)
    plt.xlabel('MCS Steps')
    plt.ylabel('c(t)')

    plt.legend(["Positive", "Negative"])
    plt.suptitle("Concentrations of positive and negative opinions")
    plt.title(f'Full Graph, N = {N}\n '
              f'Algorithm parameters - Q_A = {q_a}, Q_C = {q_c}, p = {p}, c = {c}\n'
              f'Clustering coefficient = {nx.average_clustering(G)}, Average degree = {np.mean([d for _, d in G.degree()])}')
    plt.show()

    return times, positive_conc, negative_conc

opinions(1000)