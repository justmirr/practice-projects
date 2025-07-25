import pandas as pd
from collections import Counter
from itertools import combinations

df = pd.read_csv('data/cross-selling.csv')
df['items_bought'] = df['items_bought'].apply(lambda x: x.split(","))

# get all pair combinations
pair_counts = Counter()
for items in df['items_bought']:
    pairs = combinations(sorted(items), 2)
    pair_counts.update(pairs)

def get_cross_sells(product):
    suggestions = [
        pair[1] if pair[0] == product else pair[0]
        for pair in pair_counts if product in pair
    ]              
    return list(set(suggestions))

# test cross-selling
print("if user buys laptop, suggest:", get_cross_sells('laptop'))
print("if user buys phone, suggest:", get_cross_sells('phone'))