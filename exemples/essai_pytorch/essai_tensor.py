import torch
import numpy as np

def print_tensor_attibutes(tensor):
    print(f"tensor.shape: {tensor.shape}")
    print(f"tensor.dtype : {tensor.dtype}")
    print(f"tensor.device: {tensor.device}")

#create directly tensor from data:
data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)
print(f"x_data: {x_data}")
print_tensor_attibutes(x_data);

#create indirecly tensor from numpy ndarray:
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"x_np: {x_np}")

#create tensor with random or fixed value (0 or 1):
shape = (2,3) # 2lignes , 3 colonnes
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)


print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")
print(f"Random Tensor: \n {rand_tensor} \n")
print_tensor_attibutes(rand_tensor);

#pour approfondir :
#https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
