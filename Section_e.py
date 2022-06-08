import numpy as np
import matplotlib.pyplot as plt




#First we introduce some constants and initial values that we may need

c = 3e8  #m/s

G = 6.67e-11  #m³/kgs²

hbar = 1.055e-34  #Js

Ep = np.sqrt(hbar * c**5 / G)  #J

mp = np.sqrt(hbar * c / G)

lp = np.sqrt(hbar * G / c**3)

Phii = (Ep / 2) * np.sqrt(1001/np.pi)

Psii = Phii / Ep

dPsii = 0

hi = 1

Ai = 0

dAi = 1

vi = 3 * hbar * c**5 / (8 * np.pi * G * Ep**2)

dvi = 3 * hbar * c**5 * Psii / (4 * np.pi * G * Phii**2)

N = 10000




#Then, we define the vectors that we are going to fill

tau = np.linspace(0, 100, N)

Dtau = (tau[N-1] - tau[0]) / N

v = np.zeros(N)

dv = np.zeros(N)

h = np.zeros(N)

A = np.zeros(N)

dA = np.zeros(N)

Psi = np.zeros(N)

dPsi = np.zeros(N)

d2Psi = np.zeros(N)




#After that, we introduce the initial values in the first position of each vector

v[0] = vi

dv[0] = dvi

h[0] = hi

A[0] = Ai

dA[0] = dAi

Psi[0] = Psii

dPsi[0] = dPsii

d2Psi[0] = -( 3 * hi * dPsii + dvi )




#Now, we perform the Euler's method

for i in range (0, N-1):

	d2Psi[i+1] = d2Psi[i] - Dtau*(3 * h[i] * dPsi[i] + dv[i])

	dPsi[i+1] = dPsi[i] + Dtau*d2Psi[i+1]

	Psi[i+1] = Psi[i] + Dtau*dPsi[i+1]

	dv[i+1] = dv[i] + Dtau*( 3 * hbar * c**5  * Psi[i+1] / (4 * np.pi * G * Phii**2)  )

	v[i+1] = v[i] + Dtau*dv[i+1]

	h[i+1] = np.sqrt( (8 * np.pi / 3) * ( dPsi[i+1]**2 / 2 + v[i+1] ) )

	dA[i+1] = dA[i] + Dtau*h[i+1]

	A[i+1] = A[i+1] + Dtau*dA[i+1]



#print(d2Psi)
#print(dPsi)
#print(Psi)
#print(v)
#print(h)


#And then, we plot everything and save every array in order to use them in the next section

plt.plot(tau, Psi, color = 'mediumseagreen')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\Psi$')
plt.title('Evolution of the scalar field')
plt.savefig('Figure 1.pdf')
plt.show()



plt.plot(tau, A, color = 'mediumseagreen')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$ln(a/a_i)$')
plt.title(r'Evolution of $ln(a/a_i)$')
plt.savefig('Figure 2.pdf')




with open('Psi.txt', 'wb') as f:

    np.save(f, Psi)


with open('A.txt', 'wb') as f:

    np.save(f, A)
