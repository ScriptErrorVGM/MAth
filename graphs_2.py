import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
input_data = pd.read_csv('test.csv', index_col=0)
G = nx.DiGraph(input_data.values)

nx.draw(G)
plt.show()