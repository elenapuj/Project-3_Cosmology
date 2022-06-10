import numpy as np
import matplotlib.pyplot as plt


#First we introduce some constants and initial values that we may need

Psii = 2

dPsii = 0

yi = -np.sqrt(16 * np.pi / 3) * Psii

Ai = 0

N = 1000000




#Then, we define the vectors that we are going to fill

tau = np.linspace(0, 5000, N)

Dtau = (tau[N-1] - tau[0]) / N

v = np.zeros(N)

dv = np.zeros(N)

h = np.zeros(N)

A = np.zeros(N)

Psi = np.zeros(N)

dPsi = np.zeros(N)




#After that, we introduce the initial values in the first position of some of the vectors

A[0] = Ai

Psi[0] = Psii

dPsi[0] = dPsii




#Now, we perform the Euler's method

for i in range (0, N-1):

	y = -np.sqrt(16 * np.pi / 3) * Psi[i]

	v[i] = (3 / (8 * np.pi))  * (1 / (1 - np.exp(yi))**2) * (1 - np.exp(y))**2

	dv[i] = np.sqrt(np.pi / 3) * (3 / np.pi) * (1 / (1 - np.exp(yi))**2) * np.exp(y) * (1 - np.exp(y))

	h[i] = np.sqrt( (8 * np.pi / 3) * ( dPsi[i]**2 / 2 + v[i] ) )

	A[i+1] = A[i] + Dtau*h[i]

	dPsi[i+1] = dPsi[i] - Dtau*(3 * h[i] * dPsi[i] + dv[i])

	Psi[i+1] = Psi[i] + Dtau*dPsi[i+1]




#And finally, we plot everything and save every some arrays in order to use them in the next sections

plt.plot(tau[:600000], Psi[:600000], color = 'mediumseagreen')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\Psi$')
plt.title('Evolution of the scalar field')
plt.savefig('Figure 9.pdf')
plt.show()



plt.plot(tau[:600000], A[:600000], color = 'mediumseagreen')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$ln(a/a_i)$')
plt.title(r'Evolution of $ln(a/a_i)$')
plt.savefig('Figure 10.pdf')




with open('tau2.txt', 'wb') as f:

	np.save(f, tau)


with open('Psi2.txt', 'wb') as f:

    np.save(f, Psi)


with open('A2.txt', 'wb') as f:

    np.save(f, A)


with open('dPsi2.txt', 'wb') as f:

    np.save(f, dPsi)


with open('v2.txt', 'wb') as f:

    np.save(f, v)


