import numpy as np
import matplotlib.pyplot as plt



#First we introduce some constants and initial values that we may need

c = 3e8  #m/s

G = 6.67e-11  #m³/kgs²

hbar = 1.055e-34  #Js

Ep = np.sqrt(hbar * c**5 / G)  #J

Phii = (Ep / 2) * np.sqrt(1001/np.pi)




#Now we calculate ln(a/ai) and Psi using Phi

tau = np.linspace(0, 100, 10000)

Phi_apr = Phii - ( Ep * c**2 / (4 * np.pi * Phii) ) * np.sqrt(hbar * c / G) * tau

Psi_apr = Phi_apr/Ep

A_apr = (c**2/Ep) * np.sqrt(hbar * c / G) * tau - (hbar * c**5 / (8 * np.pi * G * Phii**2) ) * tau**2




#Then we load the results from section e)

with open('Psi.txt', 'rb') as f:

    Psi = np.load(f)


with open('A.txt', 'rb') as f:

    A = np.load(f)




#And finally we plot it

plt.plot(tau, Psi, label = 'Numerical solution', color = 'mediumseagreen')
plt.plot(tau, Psi_apr, label = 'Slow-roll approximation', color = 'firebrick')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\Psi$')
plt.title('Evolution of the scalar field')
plt.legend()
plt.savefig('Figure 3.pdf')
plt.show()



plt.plot(tau, A, label = 'Numerical solution',  color = 'mediumseagreen')
plt.plot(tau, A_apr, label = 'Slow-roll approximation', color = 'firebrick')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$ln(a/a_i)$')
plt.title(r'Evolution of $ln(a/a_i)$')
plt.legend()
plt.savefig('Figure 4.pdf')
plt.show()
