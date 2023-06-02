import json
with open("../extensions.json") as ex:
    extensions = json.load(ex)

import os
files = os.listdir()
count = 0
for ex in extensions.values():
    if f"{ex}.png" not in files:
            print(ex)
            count += 1
print("-" * 10)
print(count)