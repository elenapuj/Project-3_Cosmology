import numpy as np
import matplotlib.pyplot as plt


#First we do the needed set-up

with open('Psi2.txt', 'rb') as f:

    Psi = np.load(f)


with open('A2.txt', 'rb') as f:

    A = np.load(f)


with open('epsilon.txt', 'rb') as f:

    E = np.load(f)


with open('eta.txt', 'rb') as f:

    eta = np.load(f)


with open('n.txt', 'rb') as f:

    n = np.load(f)


with open('r.txt', 'rb') as f:

    r = np.load(f)


Ntot = 2690.0297746485685




#Now we calculate the values of the desired quantities in the SRA

y = -np.sqrt(16 * np.pi / 3) * Psi

N_SRA = (3/4) * np.exp(-y)

E_SRA = (3/4) * (1 / N_SRA**2)

eta_SRA = - 1 / N_SRA

n_SRA = 1 - (2 / N_SRA)

r_SRA = 12/N_SRA**2




#For plotting, we will go first with epsilon and eta

plt.plot(N_SRA, E, label = 'Numerical solution', color = 'mediumseagreen')
plt.plot(N_SRA, E_SRA, label = 'Slow-roll approximation', color = 'firebrick')
plt.xlim([2700, -50])
plt.xlabel('N')
plt.ylabel(r'$\epsilon$')
plt.title(r'Slow-roll parameter $\epsilon$ vs N')
plt.legend()
plt.savefig('Figure 15.pdf')
plt.show()


plt.plot(N_SRA, eta, label = 'Numerical solution', color = 'mediumseagreen')
plt.plot(N_SRA, eta_SRA, label = 'Slow-roll approximation', color = 'firebrick')
plt.xlim([2700, -50])
plt.xlabel('N')
plt.ylabel(r'$\eta$')
plt.title(r'Slow-roll parameter $\eta$ vs N')
plt.legend()
plt.savefig('Figure 16.pdf')
plt.show()




#Now, we will obtain which is the position (time) of N=60 and N=50 and we will represent n vs r

for i in range (0, len(Psi)):

        if abs(A[i] - (Ntot - 60)) <= 0.01:

                pos_i = i


        if abs(A[i] - (Ntot - 50)) <= 0.01:

                pos_f = i



plt.plot(r[pos_i:pos_f], n[pos_i:pos_f], label = 'Numerical solution', color = 'mediumseagreen')
plt.plot(r_SRA[pos_i:pos_f], n_SRA[pos_i:pos_f], label = 'Slow-roll approximation', color = 'firebrick')
plt.xlabel('r')
plt.ylabel('n')
plt.title('n vs r for the Starobinsky model')
plt.legend()
plt.savefig('Figure 17.pdf')
plt.show()
