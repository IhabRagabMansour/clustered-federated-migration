"""
Model architectures: SimpleCNN (MNIST/F-MNIST), CIFAR10_CNN, ResNet.
Adapted from the Gossip project.
"""

import torch.nn as nn
import torch.nn.functional as F
from torchvision import models


class SimpleCNN(nn.Module):
    """CNN for 28x28 grayscale (MNIST / Fashion-MNIST)."""

    def __init__(self, num_classes: int = 10, input_channels: int = 1,
                 fc_hidden: int = 512, dropout: float = 0.5, input_size: int = 28):
        super().__init__()
        self.conv1 = nn.Conv2d(input_channels, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(dropout)
        feat = input_size // 4
        self.fc1 = nn.Linear(feat * feat * 64, fc_hidden)
        self.fc2 = nn.Linear(fc_hidden, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        return self.fc2(x)


class CIFAR10_CNN(nn.Module):
    """CNN for 32x32 RGB (CIFAR-10)."""

    def __init__(self, num_classes: int = 10, dropout: float = 0.5):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 128, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(128)
        self.conv3 = nn.Conv2d(128, 256, 3, padding=1)
        self.bn3 = nn.BatchNorm2d(256)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(256 * 4 * 4, 512)
        self.fc2 = nn.Linear(512, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        x = self.pool(F.relu(self.bn3(self.conv3(x))))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        return self.fc2(x)


class ResNet(nn.Module):
    def __init__(self, num_classes: int = 10, depth: int = 18, input_channels: int = 3):
        super().__init__()
        if depth == 18:
            self.model = models.resnet18(weights=None)
        elif depth == 34:
            self.model = models.resnet34(weights=None)
        elif depth == 50:
            self.model = models.resnet50(weights=None)
        else:
            raise ValueError(f"ResNet depth must be 18/34/50, got {depth}")
        if input_channels != 3:
            self.model.conv1 = nn.Conv2d(input_channels, 64, 7, stride=2, padding=3, bias=False)
        self.model.fc = nn.Linear(self.model.fc.in_features, num_classes)

    def forward(self, x):
        return self.model(x)


def create_model(architecture: str, num_classes: int, input_channels: int,
                 input_size: int = 28, depth: int = 18) -> nn.Module:
    architecture = architecture.upper()
    if architecture == "CNN":
        if input_channels == 3:
            return CIFAR10_CNN(num_classes=num_classes)
        return SimpleCNN(num_classes=num_classes, input_channels=input_channels, input_size=input_size)
    if architecture == "RESNET":
        return ResNet(num_classes=num_classes, depth=depth, input_channels=input_channels)
    raise ValueError(f"Unknown architecture: {architecture}")
