import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import pickle

N = 1000 # number of agents
msc_all = 500 # number of Monte Carlo steps
q_a = 8  # number of agents we choose if chosen agent is anticonformist
q_c = 2  # number of agents we choose if chosen agent is conformist

p = 0.2 # propability that the agent is always anticonformist
c = 0.1  # initial concentration of agents with a positive opinion

beta = 0.3 #The probability of rewiring each edge
k = [30, 50, 80, 120] #k nearest neighbors


def opinions (k, beta):

    with open('opinions.txt', 'r') as file_op:
        opinions = [int(line.strip()) for line in file_op]

    with open('behaviours.txt', 'r') as file_beh:
        behaviours = [int(line.strip()) for line in file_beh]

    time = 0
    ones_total = list()
    minus_total = list()

    G = pickle.load(open(f'graph{k}.pickle', 'rb'))

    while time <= msc_all:

        ones = list()
        minus = list()

        for t in range(N):

           i = rnd.randint(0, N-1)

           rnd_agent_bh = behaviours[i]
           neighbours = list(G.neighbors(i))

           if rnd_agent_bh == -1:

               rnd_neigh = rnd.sample(neighbours, q_a)

               neigh_ops = list()

               for l in range(len(rnd_neigh)):
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

               rnd_neigh = rnd.sample(neighbours, q_c)
               neigh_ops = list()

               for l in range(len(rnd_neigh)):
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

    plt.figure(figsize=(10, 7))
    plt.plot(times, positive_conc, negative_conc)
    plt.xlabel('MCS Steps')
    plt.ylabel('c(t)')

    plt.legend(["Positive", "Negative"])
    plt.suptitle("Concentrations of positive and negative opinions")
    plt.title(f'Watts-Strogatz - Graph parameters - K = {k}, beta = {beta}, N = {N}\n '
              f'Algorithm parameters - Q_A = {q_a}, Q_C = {q_c}, p = {p}, c = {c}')
    plt.show()

for amt in k:
    for i in range(6):
        opinions(amt, beta)