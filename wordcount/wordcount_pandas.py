import numpy as np
import pandas as pd

print('==== PANDAS WORDCOUNT ====')

text = ['Hadoop MapReduce, a disk-based big data processing engine, is being replaced by a new generation of memory-based processing frameworks, the most popular of which is Spark.', 'Spark supports Scala, Java, Python, and R.']

file_path = 'rock-and-roll-wiki.txt'
with open(file_path, "rt") as file:
    lines = [ line.strip() for line in file.readlines() ]

for tl in [text, lines]:
    words = [ (word, 1) for line in tl for word in line.split(' ') ]
    df = pd.DataFrame(words)
    counts = df.groupby(0).sum().to_records()
    [print(c) for c in counts]

print('OUTPUT OF BREEZE LIBRARY:')
print(np.zeros(5, dtype=np.float64))

print('OUTPUT OF SPIRE:')
print(np.sin(3 + 5j))
