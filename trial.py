import random
import networkx as nx
import matplotlib.pyplot as plt

def initial_opinions(x, N):
    amt_pos = int(N * x)
    opinions = [1] * amt_pos + [0] * (N - amt_pos)
    random.shuffle(opinions)
    return opinions

def create_graph(N):
    return nx.complete_graph(N)

def simulate_opinions(N, x, p, q, msc):
    G = create_graph(N)
    positive_counts = 0
    for _ in range(msc):
        opinions = initial_opinions(x, N)
        for _ in range(100):
            updated_opinions = opinions.copy()
            for agent_a in range(N):
                neighbours = list(G.neighbors(agent_a))
                rnd_neigh = random.sample(neighbours, min(q, len(neighbours)))
                neigh_ops = [opinions[ind] for ind in rnd_neigh]

                if len(set(neigh_ops)) == 1:
                    updated_opinions[agent_a] = neigh_ops[0]
                else:
                    rnd_val = random.uniform(0, 1)
                    if rnd_val <= p:
                        updated_opinions[agent_a] = 1
                    else:
                        updated_opinions[agent_a] = 0

            opinions = updated_opinions

            if all(opinion == 1 for opinion in opinions):  # If all opinions are positive
                positive_counts += 1
                break

    return positive_counts / msc

x = 0.5
msc_all = 50
q = 2
ps = [i * 0.01 for i in range(101)]
Ns = [50, 100, 150, 200]

for N in Ns:
    fractions_p = []
    for p in ps:
        fraction_positive = simulate_opinions(N, x, p, q, msc_all)
        fractions_p.append(fraction_positive)

    plt.plot(ps, fractions_p, label=f'N = {N}')

'''d) Make a plot of exit
probability E as a function of p, where exit probability E = fraction of configurations for
which a positive consensus is reached.'''

plt.xlabel('Convincing Ability (p)')
plt.ylabel('Exit Propability')
plt.title('Monte Carlo Simulation for Positive Consensus')
plt.legend()
plt.show()

