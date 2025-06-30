import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

#device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
device="cpu"
print(f"Using {device} device")

# We define our neural network by subclassing nn.Module, and initialize the neural network layers in __init__.
# Every nn.Module subclass implements the operations on input data in the forward method.

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)
'''
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
  )
)
'''

'''
To use the model, we pass it the input data. This executes the model’s forward, along with some background operations.
 Do not call model.forward() directly!

Calling the model on the input returns a 2-dimensional tensor with dim=0 corresponding to each output of 10 raw predicted values for each class,
 and dim=1 corresponding to the individual values of each output. 
 We get the prediction probabilities by passing it through an instance of the nn.Softmax module.
 Autrement dit: 
 première dimension (0) : les dix indices (de 0 à 9) des categories de produits
 seconde dimension: individual values of each ouput : ???? à priori ici "probalité pour cette catégorie" 
'''
X = torch.rand(1, 28, 28, device=device)
logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")

## transformations expliquées:

input_image = torch.rand(3,28,28) # 3 images de 28x28
print(input_image.size()) # torch.Size([3, 28, 28])


#We initialize the nn.Flatten layer to convert each 2D 28x28 image into a contiguous array of 784 pixel values
# ( the minibatch dimension (at dim=0) is maintained).
# en gros flatten transforme des sous matrices de 28x28 en tableau plat à une dimension

flatten = nn.Flatten()
flat_image = flatten(input_image)
print(flat_image.size())  #torch.Size([3, 784])

#The linear layer is a module that applies a linear transformation on the input using its stored weights and biases.
# en gros , une transformation matricielle linéaire transforme des vacteurs de taille "in" en vecteurs de taille "out"
# en conservant les proportions .
layer1 = nn.Linear(in_features=28*28, out_features=20)
hidden1 = layer1(flat_image)
print(hidden1.size())  # torch.Size([3, 20])

# nn.reLU signifie Rectified Linear Unit , ça transforme toutes les valeurs négatives à 0
# c'est une des manières d'apporter une "non-linearité" et ça permet un meilleur apprentissage avec plus de possibilités/variantes
print(f"Before ReLU: {hidden1}\n\n")
hidden1 = nn.ReLU()(hidden1)
print(f"After ReLU: {hidden1}")

#application en séquence via mm.sequential() :

seq_modules = nn.Sequential(
    flatten,
    layer1,
    nn.ReLU(),
    nn.Linear(20, 10)
)
input_image = torch.rand(3,28,28)
logits = seq_modules(input_image)
print(f"logits (result of nn.Sequentiel(...) : {logits}")

'''
Vocabulaire :
Logits are the outputs of a neural network before the activation function is applied. 
They are the unnormalized probabilities of the item belonging to a certain class
----
The logit function is mathematically defined as the logarithm of the odds of the probability p of a certain event occurring: 
odds : chances (de proba ) pour qu'un évenement survienne
Logit(p) = log/ln(p / (1 - p)) Here, p represents the probability of the event, and log or ln denotes the natural logarithm
'''

#The last linear layer of the neural network returns logits - raw values in [-infty, infty] - which are passed to the nn.Softmax module.
# The logits are scaled to values [0, 1] representing the model’s predicted probabilities for each class.
# dim parameter indicates the dimension along which the values must sum to 1.
# en gros nn.Softmax générère des résultats de type "probabilités selon classe" et la somme des probas doit être égales à 1
softmax = nn.Softmax(dim=1)
pred_probab = softmax(logits)
print(f"logits (result of nn.Softmax(...) : {pred_probab}")

# Model Parameters:

'''
Les pondérations et les biais sont des éléments essentiels des modèles d'apprentissage automatique, en particulier dans les réseaux neuronaux. 
Les pondérations déterminent la force des connexions entre les neurones et représentent l'importance des caractéristiques d'entrée, 
tandis que les biais permettent d'affiner et d'ajuster les prédictions
idée à préciser/peaufiner/ajuster/clarifier : y=ax+b où a = pondération/weight et b = biais   ????
pondérations initiales pour nn.Linear() : k=1/in_features_size et u (-sqrt(k) , sqrt(k)) ???? coeff binomial ou autre ????
'''

'''
Many layers inside a neural network are parameterized, i.e. have associated weights and biases that are optimized during training. 
Subclassing nn.Module automatically tracks all fields defined inside your model object, 
and makes all parameters accessible using your model’s parameters() or named_parameters() methods:
'''

#In this example, we iterate over each parameter, and print its size and a preview of its values:

print(f"Model structure: {model}\n\n")

for name, param in model.named_parameters():
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")

'''
Results/outputs:
------
Model structure: NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
  )
)


Layer: linear_relu_stack.0.weight | Size: torch.Size([512, 784]) | Values : tensor([[ 0.0287, -0.0263,  0.0196,  ..., -0.0321,  0.0039,  0.0062],
        [ 0.0136,  0.0211, -0.0122,  ..., -0.0256, -0.0043,  0.0317]],
       grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.0.bias | Size: torch.Size([512]) | Values : tensor([-0.0283, -0.0106], grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.2.weight | Size: torch.Size([512, 512]) | Values : tensor([[ 0.0006,  0.0320, -0.0051,  ..., -0.0249,  0.0255, -0.0157],
        [ 0.0272,  0.0409, -0.0331,  ..., -0.0346, -0.0430, -0.0291]],
       grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.2.bias | Size: torch.Size([512]) | Values : tensor([0.0313, 0.0035], grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.4.weight | Size: torch.Size([10, 512]) | Values : tensor([[ 0.0246, -0.0197, -0.0073,  ..., -0.0316,  0.0177,  0.0437],
        [ 0.0404, -0.0331, -0.0034,  ...,  0.0221, -0.0199, -0.0403]],
       grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.4.bias | Size: torch.Size([10]) | Values : tensor([ 0.0192, -0.0153], grad_fn=<SliceBackward0>)
'''