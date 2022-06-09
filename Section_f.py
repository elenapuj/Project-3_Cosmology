import numpy as np
import matplotlib.pyplot as plt



#First we introduce some constants and initial values that we may need and also load the needed arrays from section e)

c = 3e8  #m/s

G = 6.67e-11  #m³/kgs²

hbar = 1.055e-34  #Js

Psii = np.sqrt(1001/np.pi) / 2

with open('Psi.txt', 'rb') as f:

    Psi = np.load(f)


with open('A.txt', 'rb') as f:

    A = np.load(f)


with open('tau.txt', 'rb') as f:

    tau = np.load(f)




#Now we calculate ln(a/ai) and Psi

Psi_SRA = Psii - tau / (4 * np.pi * Psii)

A_SRA = tau - tau**2 / (8 * np.pi * Psii**2)




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
