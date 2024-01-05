import pandas as pd
from pyvis.network import Network

file = f"kg.csv"
df = pd.read_csv(file, sep=',', comment='#')

nw = Network(height='100%', width='100%', bgcolor='white', directed=True)
nw.force_atlas_2based(spring_length=100)
# nw.barnes_hut()
node_size = 16
node_font = "16px sans-serif maroon"
edge_font = "16px sans-serif navy"
for index, row in df.iterrows():
    src = row['head']
    dst = row['tail']
    edge_label = row['predicate']
    nw.add_node(src, size=node_size, group=row['head_type'], font=node_font)
    nw.add_node(dst, size=node_size, group=row['tail_type'], font=node_font)
    nw.add_edge(src, dst, label=edge_label, font=edge_font)

nw.set_edge_smooth('dynamic')
nw.show('kg.html')
