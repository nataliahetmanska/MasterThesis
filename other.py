import random as rnd
import networkx as nx
import matplotlib.pyplot as plt

N = 10000  # number of agents
msc_all = 500 # number of Monte Carlo steps
q_a = 8  # number of agents we choose if chosen agent is anticonformist
q_c = 2  # number of agents we choose if chosen agent is conformist

p = 0.2  # propability that the agent is always anticonformist
c = 0.8  # initial concentration of of agents with a positive opinion
prop = 0.15


def create_graph(N):
   #watts_strogatz = nx.watts_strogatz_graph(N, q, prop)
   graph = nx.complete_graph(N)
   return graph

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

opinions = initial_opinions(c, N)
behaviours = initial_behaviours(p, N)

t = 0  # time counter

conf_pos = list()
conf_neg = list()
ant_pos = list()
ant_neg = list()

G = create_graph(N)

while t <= msc_all:

   i = rnd.randint(0, N-1)

   rnd_agent_op = opinions[i]
   rnd_agent_bh = behaviours[i]

   if rnd_agent_bh == -1:

       neighbours = list(G.neighbors(i))

       rnd_neigh = rnd.sample(neighbours, q_a)

       neigh_ops = list()

       for l in range(len(rnd_neigh)):
           neigh_ops.append(opinions[rnd_neigh[l]])

           if len(set(neigh_ops)) == 1:
               if neigh_ops[0] == 1:
                   opinions[i] = -1
               else:
                   opinions[i] = opinions[i]
               anty_plus_amt = 0
               conf_plus_amt = 0

               for i in range(len(opinions)):
                   if behaviours[i]==1:
                       if opinions[i]==1:
                           conf_plus_amt = conf_plus_amt+1
                   if behaviours[i] == -1:
                       if opinions[i] == 1:
                           anty_plus_amt = anty_plus_amt + 1


               conf_pos.append(conf_plus_amt)
               ant_pos.append(anty_plus_amt)
               t = t + 1

           else:
               anty_plus_amt = 0
               conf_plus_amt = 0
               for i in range(len(opinions)):
                   if behaviours[i] == 1:
                       if opinions[i] == 1:
                           conf_plus_amt = conf_plus_amt + 1
                   if behaviours[i] == -1:
                       if opinions[i] == 1:
                           anty_plus_amt = anty_plus_amt + 1

               conf_pos.append(conf_plus_amt)
               ant_pos.append(anty_plus_amt)
               t = t + 1

   if rnd_agent_bh == 1:

       neighbours = list(G.neighbors(i))
       rnd_neigh = rnd.sample(neighbours, q_c)
       neigh_ops = list()

       for l in range(len(rnd_neigh)):
           neigh_ops.append(opinions[rnd_neigh[l]])

           if len(set(neigh_ops)) == 1:
               if neigh_ops[0] == 1:
                   opinions[i] = -1
               else:
                   opinions[i] = opinions[i]

               anty_plus_amt = 0
               conf_plus_amt = 0
               for i in range(len(opinions)):
                   if behaviours[i] == 1:
                       if opinions[i] == 1:
                           conf_plus_amt = conf_plus_amt + 1
                   if behaviours[i] == -1:
                       if opinions[i] == 1:
                           anty_plus_amt = anty_plus_amt + 1

               conf_pos.append(conf_plus_amt)
               ant_pos.append(anty_plus_amt)
               t = t + 1
           else:
               anty_plus_amt = 0
               conf_plus_amt = 0
               for i in range(len(opinions)):
                   if behaviours[i] == 1:
                       if opinions[i] == 1:
                           conf_plus_amt = conf_plus_amt + 1
                   if behaviours[i] == -1:
                       if opinions[i] == 1:
                           anty_plus_amt = anty_plus_amt + 1

               conf_pos.append(conf_plus_amt)
               ant_pos.append(anty_plus_amt)
               t = t + 1



times = list(range(1, len(conf_pos)+1))


print(conf_pos)

positive_conc_conf = list()
positive_conc_anty = list()


for i in conf_pos:
    count = behaviours.count(1)
    positive_conc_conf.append(i/count)

for i in ant_pos:
    positive_conc_anty.append(i/behaviours.count(-1))

plt.plot(times, positive_conc_conf, positive_conc_anty)
plt.show()

