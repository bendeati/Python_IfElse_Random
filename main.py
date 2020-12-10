# Elágazások használata

szam = -10;
if szam > 0:
    print(f"A(z) {szam} nagyobb mint nulla!")
    print("A(z)", szam, "nagyobb mint nulla!")
elif szam < 0:
    print(f"A(z) {szam} kisebb mint nulla!")
else:
    print(f"A szám pont nulla!")

import random

vSzam = random.randint(-5, 5)
print(f"Egy véletlen szám: {vSzam}")
if vSzam > 0:
    print(f"A(z) {vSzam} nagyobb mint nulla!")
    print("A(z)", vSzam, "nagyobb mint nulla!")
elif vSzam < 0:
    print(f"A(z) {vSzam} kisebb mint nulla!")
else:
    print(f"A szám pont nulla!")
