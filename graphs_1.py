import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt

graph = nx.Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')

def add_edge(f_item, s_item, graph=None):
  graph.add_edge(f_item, s_item)
  graph.add_edge(s_item, f_item) 

add_edge('A', 'B', graph=graph)
add_edge('B', 'C', graph=graph)
add_edge('B', 'D', graph=graph)
add_edge('D', 'E', graph=graph)

nx.draw_circular(graph,
         node_color='red',
         node_size=1000,
         with_labels=True)

plt.show()

def complete_graph(N: int) -> nx.Graph:
  graph = nx.Graph()
   
  N_range = range(N)
   
  all_pairs = itertools.permutations(N_range, 2)
   
  graph.add_nodes_from(N_range)
  graph.add_edges_from(all_pairs)
   
  return graph

graph = complete_graph(['A','B','C','D','E'])

nx.draw_circular(graph, 
         node_color='y',
         node_size=750,
         with_labels=True)

plt.show()