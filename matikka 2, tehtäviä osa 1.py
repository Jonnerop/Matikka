import numpy as np
from fractions import Fraction

# tehtävä 1.1.

a = 2.493
b = 0.911

a1=(np.degrees(a))
a2=(np.degrees(b))
print("Tehtävä 1.1.")
print(f"{a1:.4}°")
print(f"{a2:.4}°")

# tehtävä 1.2

c = 137.7
d = 62.3

a3 = (np.radians(c))
a4 = (np.radians(d))
print()
print("Tehtävä 1.2.")
print(f"{a3:.4} rad")
print(f"{a4:.4} rad")
print()
print("Tehtävä 1.3.")
# tehtävä 1.3
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
    radians = np.radians(i) / np.pi
    fraction = Fraction(radians).limit_denominator()
    print(f"{i}° astetta on {fraction}π radiaania")

# tehtävä 2.1.
print()
print("Tehtävä 2.1.")
a5 = 1.6
b2 = 2.3

c2 = np.sqrt(a5**2 + b2**2)
print(f"Hypotenuusan pituus on {c2:.3}")
