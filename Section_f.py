import numpy as np
import matplotlib.pyplot as plt



#First we load the needed arrays from section e)

with open('Psi1.txt', 'rb') as f:

    Psi = np.load(f)


with open('A1.txt', 'rb') as f:

    A = np.load(f)


with open('tau1.txt', 'rb') as f:

    tau = np.load(f)




#Now we calculate ln(a/ai) and Psi

Psi_SRA = Psi[0] - tau / (4 * np.pi * Psi[0])

A_SRA = tau - tau**2 / (8 * np.pi * Psi[0]**2)




#And finally we plot it

plt.plot(tau[:37500], Psi[:37500], label = 'Numerical solution', color = 'mediumseagreen')
plt.plot(tau[:37500], Psi_SRA[:37500], label = 'Slow-roll approximation', color = 'firebrick')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\Psi$')
plt.title('Evolution of the scalar field')
plt.legend()
plt.savefig('Figure 3.pdf')
plt.show()



plt.plot(tau[:37500], A[:37500], label = 'Numerical solution',  color = 'mediumseagreen')
plt.plot(tau[:37500], A_SRA[:37500], label = 'Slow-roll approximation', color = 'firebrick')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$ln(a/a_i)$')
plt.title(r'Evolution of $ln(a/a_i)$')
plt.legend()
plt.savefig('Figure 4.pdf')
plt.show()
