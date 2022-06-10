import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


#First we load the arrays needed from e)

with open('A1.txt', 'rb') as f:

    A = np.load(f)


with open('tau1.txt', 'rb') as f:

    tau = np.load(f)



#Now, we do a linear regression of ln(a/a_i) vs ln(tau) out of the last 125000 data of our numerical simulation. The slope should be p

r = stats.linregress(np.log(tau[875000:]), A[875000:])

p = r.slope

print('p=', p)
