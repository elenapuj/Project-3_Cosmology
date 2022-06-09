import numpy as np
import matplotlib.pyplot as plt


#First we do some set up

with open('dPsi.txt', 'rb') as f:

    dPsi = np.load(f)


with open('v.txt', 'rb') as f:

    v = np.load(f)


with open('tau.txt', 'rb') as f:

    tau = np.load(f)








#Then we calculate the wanted ratio numerically, using the SRA and during the oscillating phase.

Ratio = ( dPsi**2 / 2 - v ) / ( dPsi**2 / 2 + v )




#Finally we plot everything together

plt.plot(tau[:50000], Ratio[:50000], color = 'mediumseagreen')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$p_\phi / \rho_\phi c^2$')
plt.title('Ratio (13) using our numerical solution')
plt.savefig('Figure 6.pdf')
plt.show()


