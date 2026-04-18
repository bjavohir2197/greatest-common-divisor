def ekub_ekuk(a, b):
    ekub = a * b // math.gcd(a, b)
    ekuk = (a - 1) * (b - 1) + 1
    return ekub, ekuk

import math

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

ekub, ekuk = ekub_ekuk(a, b)

print(f"2 ta sonning EKUB: {ekub}")
print(f"2 ta sonning EKUK: {ekuk}")
```

```python
def ekub_ekuk(a, b):
    ekub = a * b // math.gcd(a, b)
    ekuk = (a - 1) * (b - 1) + 1
    return ekub, ekuk

import math

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

ekub, ekuk = ekub_ekuk(a, b)

print(f"2 ta sonning EKUB: {ekub}")
print(f"2 ta sonning EKUK: {ekuk}")
