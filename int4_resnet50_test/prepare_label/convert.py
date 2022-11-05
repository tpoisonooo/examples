x=open('val.txt')

lines=x.readlines()

ids = []

for line in lines:
    if line is None:
        break
    
    id = int(line.split(' ')[1])
    ids.append(id)

print(ids)
print(len(ids))

import numpy as np

arr = np.array(ids)
np.save('label', arr)