import os
import json
from collections import Counter

# wait until all mapper json files exist
while True:
    files = [f for f in os.listdir("counters") if f.endswith(".json")]
    if len(files) == 9:
        break

# combine all  mapper outputs
total = Counter()
for i in range(1, 10):
    path = os.path.join("counters", f"{i}.json")
    with open(path) as f:
        data = json.load(f)
        total.update(data)

# sort
ordered = dict(sorted(total.items(), key=lambda x: x[1], reverse=True))
#ordered = dict(sorted(total.items(), key=lambda x: (-x[1], x[0])))

# save totals
os.makedirs("counters", exist_ok=True)
with open(os.path.join("counters", "total_counts.json"), "w") as f:
    json.dump(ordered, f)

print("Reducer done")