import os
import pandas as pd

file_path = os.path.join('data', 'words.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()

word_tuples = []
for line in lines:
    line = line.strip()
    
    separate = line.split(",")

    if len(separate) == 1:
        word, classification = line.split(" ")
    else:
        t = line.split(" ")
        word = t[0]
        classification = " ".join(t[1:])

    word_tuples.append((word, classification))

df = pd.DataFrame(word_tuples, columns=['word', 'classification'])
df.to_csv("data/words.csv", index=False)
