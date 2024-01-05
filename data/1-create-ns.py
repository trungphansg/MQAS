import pandas as pd

file = f"kg.csv"
df = pd.read_csv(file, sep=',', comment='#')
out_file = f"ns.csv"

df = df[['head_type','predicate','tail_type']].drop_duplicates()
print(df.shape[0])
print(df)

df.to_csv(out_file, index=False, sep=',')