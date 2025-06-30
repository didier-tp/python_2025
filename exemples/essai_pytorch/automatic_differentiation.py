import torch

'''
When training neural networks, the most frequently used algorithm is back propagation. 
In this algorithm, parameters (model weights) are adjusted according to the gradient of the loss function with respect to the given parameter.

To compute those gradients, PyTorch has a built-in differentiation engine called torch.autograd.
 It supports automatic computation of gradient for any computational graph.
 
 Consider the simplest one-layer neural network,
  with input x, parameters w and b, and some loss function. 
  It can be defined in PyTorch in the following manner:
'''

x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True)  # w = weigh parameter (to optimize)
b = torch.randn(3, requires_grad=True) # b = bias parameter (to optimize)
z = torch.matmul(x, w)+b  #  z=x*w+b
#loss = fruit d'une comparaison entre attendu y et calculé z
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

print(f"Gradient function for z = {z.grad_fn}")
print(f"Gradient function for loss = {loss.grad_fn}")

'''
loss signifie "perte" en francais
synomyme de "loss function" : "cost function" , "error function" , 
valeur à minimiser pour que res_calcul soit au plus près du résultat attendu

basic/simple/trivial loss function:  abs(y_pred - y_actual)

'''