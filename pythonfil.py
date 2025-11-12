print("hej")
import numpy as np

Km = 0.155
b =  0.0025
jm = 9e-4
jh = 2.5e-4
j = jm + jh
Ra = 2.4
La = 0.25e-3
Ku = 0.3078
Ka = Ku

T1 = -((b* La) + (j * Ra)) / (2*j*Ku)
T2 = ((b*La + j*Ra) / (2 *j *Ku))**2 - (Km + b*Ra + Ka * Km)/(j*Ka)

print("T1, real del för roten", T1)
print("T2, imaginär del för roten", T2)
# s = T1 + T2

