
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt


# datasets.FashionMNIST is a subclass of torch.utils.data.Dataset

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
'''
        root is the path where the train/test data is stored,
        train specifies training or test dataset,
        download=True downloads the data from the internet if it’s not available at root.
        transform and target_transform specify the feature and label transformations

        if root="data" --> local subdirectory "data" in python project
'''

print(f"first entry in training_data (at index 0): ${training_data[0]}")
# $(tensor([[[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
# ...     0.0000, 0.0000, 0.0000, 0.0000]]]), 9)
# soit liste avec tensor à trois dimensions et indice de catégorie de produit (ex: 9 pour "ankle boot" )


labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()

#En gros , dataset = jeux de données (très spécifique , au cas par cas)
#dataLoader = élément technique capable d'effectuer rapidement des extractions de parties de données
#dans un contexte de boucles (avec itérations efficaces et souvent répétées):

from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
# suffle signifie mélanger , batchèsize=64 par paquets de 64

# Display image and label index via dataloader:
train_features, train_labels = next(iter(train_dataloader))
print(f"Feature batch shape: {train_features.size()}")  #torch.Size([64, 1, 28, 28])
print(f"Labels batch shape: {train_labels.size()}") #torch.Size([64])
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="gray")
plt.show()
print(f"Label: {label}") #Label: 7