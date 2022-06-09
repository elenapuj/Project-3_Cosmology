import numpy as np
import matplotlib.pyplot as plt




#First we introduce some constants and initial values that we may need

Psii = np.sqrt(1001/np.pi) / 2

dPsii = 0

Ai = 0

N = 1000000




#Then, we define the vectors that we are going to fill

tau = np.linspace(0, 40000, N)

Dtau = (tau[N-1] - tau[0]) / N

v = np.zeros(N)

dv = np.zeros(N)

h = np.zeros(N)

A = np.zeros(N)

Psi = np.zeros(N)

dPsi = np.zeros(N)




#After that, we introduce the initial values in the first position of each vector

A[0] = Ai

Psi[0] = Psii

dPsi[0] = dPsii




#Now, we perform the Euler's method

for i in range (0, N-1):

	dv[i] = 3 * Psi[i] / (4 * np.pi * Psii**2)

	v[i] = 3 * Psi[i]**2 / (8 * np.pi * Psii**2)

	h[i] = np.sqrt( (8 * np.pi / 3) * ( dPsi[i]**2 / 2 + v[i] ) )

	A[i+1] = A[i] + Dtau*h[i]

	dPsi[i+1] = dPsi[i] - Dtau*(3 * h[i] * dPsi[i] + dv[i])

	Psi[i+1] = Psi[i] + Dtau*dPsi[i+1]



#print(d2Psi)
#print(dPsi)
#print(Psi)
#print(v)
#print(h)


#And then, we plot everything and save every array in order to use them in the next sections

plt.plot(tau[:37500], Psi[:37500], color = 'mediumseagreen')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\Psi$')
plt.title('Evolution of the scalar field')
plt.savefig('Figure 1.pdf')
plt.show()



plt.plot(tau[:37500], A[:37500], color = 'mediumseagreen')
plt.vlines(tau[24344], A[0], A[37500], color = 'firebrick')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$ln(a/a_i)$')
plt.title(r'Evolution of $ln(a/a_i)$')
plt.savefig('Figure 2.pdf')




with open('tau.txt', 'wb') as f:

	np.save(f, tau)


with open('Psi.txt', 'wb') as f:

    np.save(f, Psi)


with open('A.txt', 'wb') as f:

    np.save(f, A)


with open('dPsi.txt', 'wb') as f:

    np.save(f, dPsi)


with open('v.txt', 'wb') as f:

    np.save(f, v)


