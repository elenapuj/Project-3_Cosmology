import numpy as np
import matplotlib.pyplot as plt


#First, we load both Psi and ln(a/a_i). We also define Ntot

with open('Psi.txt', 'rb') as f:

    Psi = np.load(f)


with open('A.txt', 'rb') as f:

    A = np.load(f)


Ntot = 501.3962539723227




#Now we calculate both epsilon and N

E = 1 / (4 * np.pi * Psi**2)

N = Ntot - A




#Finally, we plot them

plt.plot(N[:25000], E[:25000], color = 'mediumseagreen')
plt.xlim([500, -10])
plt.xlabel('N')
plt.ylabel(r'$\epsilon$')
plt.title(r'Slow-roll parameter $\epsilon$ vs N')
plt.savefig('Figure 7.pdf')
plt.show()

