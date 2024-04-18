import torch
import numpy as np

print("\n\nPonte com NumPy\n\n")

# Tensor para matriz Numpy
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

# Uma mudança no tensor reflete na matriz NumPy
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

# Matriz NumPy para tensor
n = np.ones(5)
t = torch.from_numpy(n)

# As alterações na matriz Numpy refletem no tensor
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")
