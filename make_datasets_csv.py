import os
from pathlib import Path
import csv
import pandas as pd
import numpy as np

f = open('/home/kwon/sparse/data/custom/dataset_val.csv','w',newline='')
wr = csv.writer(f)

#path = Path('/home/kwon/다운로드/nyu2_test.csv')
#file = path.read_text()

p = Path('/home/kwon/sparse/data/custom/val/')
[x for x in p.iterdir() if x.is_dir()]
list1 = list(p.glob('**/*.jpg.npy'))
list2 = list(p.glob('**/*.png.npy'))

c = sorted(list1)
d = sorted(list2)
print(*c, sep = '\n')
print(*d, sep = '\n')
for w in range(len(list1)):
 wr.writerow([c[w], d[w]])
#wr.writerow(d)

f.close()