import numpy as np
import matplotlib.pyplot as plt



#First we load the needed arrays and calculate epsilon

with open('A1.txt', 'rb') as f:

	A = np.load(f)


with open('Psi1.txt', 'rb') as f:

	Psi = np.load(f)


E = 1 / (4 * np.pi * Psi**2)




#With epsilon we calculate r and n

n = 1 - 4 * E

r = 16 * E




#Now we calculate the positions at which N=60 and N=50

for i in range (0, len(Psi)):

	if abs(A[i] - 440) <= 0.01:

		pos_i = i


	if abs(A[i]-450) <= 0.01:

		pos_f = i




#Finally, we plot them in the desired interval

plt.plot(r[pos_i:pos_f], n[pos_i:pos_f], color = 'mediumseagreen')
plt.xlabel('r')
plt.ylabel('n')
plt.title(r'n vs r for the $\Phi^2$-model')
plt.savefig('Figure 8.pdf')
plt.show()
