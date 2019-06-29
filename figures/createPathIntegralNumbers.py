import numpy as np

n = 25
mu = 45
std = 40

inTheta = np.random.normal(mu, std, n)
outTheta = np.random.normal(mu+180, std, n)

strength = ((inTheta-45) - (outTheta-180-45))
normalizedStrength = np.abs(strength)/np.max(np.abs(strength))

# print (outTheta)
# print (inTheta)
# print (strength)

for i,j,k in zip(inTheta, outTheta, normalizedStrength):
     print("{%.4f/%.4f/%.4f}," % (i,j,k))