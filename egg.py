# Exercise 1.12 How to cook the perfect egg
# Andrew Turner

#First import needed programs and define variables.

from math import log, pi

rho = 1.038     # Egg density (g cm^-3)
c = 3.7         # Specific heat capacity (J g^-1 K^-1)
K = 5.4*10**-3  # Thermal conductivity (W cm^-1 K^-1)
Tw = 100.       # Boiling water temperature (C)
Ty = 70.        # Desired yolk temperature (C)

#Begin calculations!

#Temperature of egg from fridge
T0 = 4.

# Weight of small egg (g)
M = 47.

tsmall = M ** (2.0 / 3) * c * rho ** (1.0 / 3) / \
    (K * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * \
    log(0.76 * (T0 - Tw) / (Ty - Tw))

# Weight of large egg (g)
M = 67.

tlarge = M ** (2.0 / 3) * c * rho ** (1.0 / 3) / \
    (K * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * \
    log(0.76 * (T0 - Tw) / (Ty - Tw))

print """\

To hard boil an egg out of the refrigerator: 
Cook a small egg for %.2f minutes. 
Cook a large egg for %.2f minutes.

""" % (tsmall / 60, tlarge / 60)

# Room temperature egg
T0 = 20.

# Weight of small egg (g)
M = 47.

tsmall = M ** (2.0 / 3) * c * rho ** (1.0 / 3) / \
    (K * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * \
    log(0.76 * (T0 - Tw) / (Ty - Tw))

# Weight of large egg (g)
M = 67.

tlarge = M ** (2.0 / 3) * c * rho ** (1.0 / 3) / \
    (K * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * \
    log(0.76 * (T0 - Tw) / (Ty - Tw))

print """\

To hard boil an egg at room temperature:
Cook a small egg for %.2f minutes.
Cook a large egg for %.2f minutes.

""" % (tsmall / 60, tlarge / 60)

