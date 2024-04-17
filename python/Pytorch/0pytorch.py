import torch
import numpy as np

# Diretamente dos dados
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(f"x_data: \n {x_data} \n")

# A partir de arrays NumPy
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"x_np: \n {x_np} \n")

# De outro tensor
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

# Saida:
# x_data:
# tensor([[1, 2], [3, 4]])

# Com valores aleatorios ou constantes
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")

# atributos de um tensor
tensor = torch.rand(3, 4)
print(f"shape of tensor: {tensor.shape}") # torch.Size([3, 4])
print(f"dtype of tensor: {tensor.dtype}") # torch.float32
print(f"device tensor is stored on: {tensor.device}") # cpu

# operações em tensores

if torch.cuda.is_available():
    tensor = tensor.to("cuda")

tensor[:,1] = 0 # atribui 0 em todos os elementos da coluna 1 do tensor

# união dos elementos
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

# operações matematicas
# multiplicação de matrizes
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)
y3 = torch.rand_like(tensor)
torch.matmul(tensor, tensor.T, out=y3)
print(f"y1: {y1}")

# multiplicação elemento por elemento
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
print(f"z1: {z1}")