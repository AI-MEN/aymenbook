#!/usr/bin/env python
# coding: utf-8

# # 2

# In[1]:


markd = 'concept2.md'


# In[2]:


from utils import find_recursive_parents
import networkx as nx
import matplotlib.pyplot as plt

list_paires=[]
parents = find_recursive_parents(markd, list_paires)     
#print (parents)
G = nx.DiGraph()
G.add_edges_from(parents, label="parent")
nx.draw(G, with_labels=True)
plt.show()


# ```{include} ./concept2.md
# ```
