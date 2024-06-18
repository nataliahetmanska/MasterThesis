import random as rnd

p = 0.2 # propability that the agent is always anticonformist
c = 0.1  # initial concentration of agents with a positive opinion
N = 1000

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

ops = initial_opinions(c, N)
beh = initial_behaviours(p, N)

file_ops = open('opinions.txt','w')
for opinion in ops:
	file_ops.write(str(opinion)+"\n")
file_ops.close()

file_beh = open('behaviours.txt','w')
for behav in beh:
	file_beh.write(str(behav)+"\n")
file_beh.close()