import numpy as np
import matplotlib.pyplot as plt


#We load the needed arrays from e) and calculate epsilon

with open('Psi1.txt', 'rb') as f:

    Psi = np.load(f)


with open('tau1.txt', 'rb') as f:

    tau = np.load(f)



E = 1 / (4 * np.pi * Psi**2)



#Then we plot it

plt.plot(tau[:25000], E[:25000], color = 'mediumseagreen')
plt.hlines(1, 0, tau[25000], color = 'firebrick')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\epsilon$')
plt.title(r'Slow-roll parameter $\epsilon$')
plt.savefig('Figure 5.pdf')
plt.show()




#Now we find the value of tau for which epsilon is 1

for i in range (0, len(tau)):

	if abs(E[i] - 1) <= 0.001:

		E_max = E[i]
		pos_max = i


print('i=', pos_max)
print('E=', E_max)
print('tau=', tau[pos_max])



#And then we calculate Ntot using ln(a/a_i)

with open('A1.txt', 'rb') as f:

    A = np.load(f)


Ntot = A[pos_max]


print('N_tot=', Ntot)




#Finally we calculate the SRA value

Ntot_SRA = Psi[0]**2 * 2 * np.pi - 1/2

print('N_tot_SRA=', Ntot_SRA)
