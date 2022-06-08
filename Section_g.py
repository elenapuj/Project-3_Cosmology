import numpy as np
import matplotlib.pyplot as plt




#We load the array for Psi and use it to calculate epsilon

with open('Psi.txt', 'rb') as f:

    Psi = np.load(f)


E = 1 / (4 * np.pi * Psi**2)

tau = np.linspace(0, 425, 10000)




#Then we plot it

plt.plot(tau, E, color = 'mediumseagreen')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\epsilon$')
plt.title(r'Slow-roll parameter $\epsilon$')
plt.savefig('Figure 5.pdf')
plt.show()




#Now we find the value of tau for which epsilon is 1

for i in range (0, 10000):

	if abs(E[i] - 1) <= 0.01:

		E_max = E[i]
		pos_max = i




#And then we calculate Ntot using ln(a/a_i)

Ntot = (1/2) * ( (Psi[0]/Psi[pos_max])**2 - 1  )


print('N_tot=', Ntot)




#Finally we calculate the SRA value

Ntot_apr = Psi[0]**2 * 2 * np.pi - 1/2

print('N_tot_appr=', Ntot_apr)
