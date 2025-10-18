import json
import sys
import os
import string
from collections import Counter

i = sys.argv[1]

# check output folder exists
os.makedirs("counters", exist_ok=True)

with open(f"titles/{i}.txt") as f:
    text = f.read().lower()

# format
for ch in string.punctuation:
    text = text.replace(ch, " ")

words = text.split()

counts = Counter(words)

# save counts to json
with open(f"counters/{i}.json", "w") as f:
    json.dump(counts, f)

print(f"Mapper {i} done, wrote {len(counts)} unique words")