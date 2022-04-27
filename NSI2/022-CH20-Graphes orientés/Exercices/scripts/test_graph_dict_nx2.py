from graph_dict_nx import *
from random import randint
n = 20

G=GraphDict([i for i in range(n)])
for i in range(n):
    for j in range(n):
        if i!=j and randint(0,n//2)==0:
            G.add_arrow(i,j)


G.draw()