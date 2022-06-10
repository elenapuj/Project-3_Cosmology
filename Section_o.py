import numpy as np
import matplotlib.pyplot as plt


#INITIAL SET UP

#We load the needed arrays from e)

with open('Psi2.txt', 'rb') as f:

    Psi = np.load(f)


with open('A2.txt', 'rb') as f:

	A = np.load(f)


with open('tau2.txt', 'rb') as f:

    tau = np.load(f)






#REPETITION OF SECTION g)


#We first calculate epsilon

y = -np.sqrt(16 * np.pi / 3) * Psi

E = (4/3) * np.exp(2 * y) / (1 - np.exp(y))**2



#Then we plot it

plt.plot(tau[:539000], E[:539000], color = 'mediumseagreen')
plt.hlines(1, 0, tau[540000], color = 'firebrick')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\epsilon$')
plt.title(r'Slow-roll parameter $\epsilon$')
plt.savefig('Figure 11.pdf')
plt.show()




#Now we find the value of tau for which epsilon is 1

for i in range (0, len(tau)):

	if abs(E[i] - 1) <= 0.001:

		E_max = E[i]
		pos_max = i


print('i=', pos_max)
print('E=', E_max)
print('tau=', tau[pos_max])



#And finally we calculate Ntot using ln(a/a_i)

Ntot = A[pos_max]

print('N_tot=', Ntot)






#REPETITION OF SECTION k)


#Now we have already calculated epsilon so only eta and N are left

eta = (4/3) * (2 * np.exp(2 * y) - np.exp(y)) / (1 - np.exp(y))**2

N = Ntot - A




#Finally, we plot them and save epsilon and eta in order to compare them to the SRA in the next section

plt.plot(N, E, color = 'mediumseagreen')
plt.xlim([2700, -50])
plt.xlabel('N')
plt.ylabel(r'$\epsilon$')
plt.title(r'Slow-roll parameter $\epsilon$ vs N')
plt.savefig('Figure 12.pdf')
plt.show()


plt.plot(N, eta, color = 'mediumseagreen')
plt.xlim([2700, -50])
plt.xlabel('N')
plt.ylabel(r'$\eta$')
plt.title(r'Slow-roll parameter $\eta$ vs N')
plt.savefig('Figure 13.pdf')
plt.show()



with open('epsilon.txt', 'wb') as f:

        np.save(f, E)


with open('eta.txt', 'wb') as f:

    np.save(f, eta)






#REPETITION OF SECTION l)


#With epsilon and eta we calculate r and n

n = 1 - 6 * E + 2 * eta

r = 16 * E




#Now we calculate the positions (times) at which N=60 and N=50

for i in range (0, len(Psi)):

        if abs(A[i] - (Ntot - 60)) <= 0.01:

                pos_i = i


        if abs(A[i] - (Ntot - 50)) <= 0.01:

                pos_f = i




#Finally, we plot them in the desired interval and save them

plt.plot(r[pos_i:pos_f], n[pos_i:pos_f], color = 'mediumseagreen')
plt.xlabel('r')
plt.ylabel('n')
plt.title('n vs r for the Starobinsky model')
plt.savefig('Figure 14.pdf')
plt.show()



with open('n.txt', 'wb') as f:

        np.save(f, n)


with open('r.txt', 'wb') as f:

    np.save(f, r)
