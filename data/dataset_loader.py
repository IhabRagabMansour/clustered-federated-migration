"""
Dataset loading for MNIST / Fashion-MNIST / CIFAR-10.
Adapted (trimmed) from the Gossip project.
"""

import os
from typing import Tuple

from torchvision import datasets, transforms
from torch.utils.data import Dataset


class DatasetLoader:
    def __init__(self, dataset_name: str, data_path: str = "./data/datasets"):
        self.dataset_name = dataset_name.upper()
        self.data_path = data_path
        os.makedirs(self.data_path, exist_ok=True)

        valid = ["MNIST", "F-MNIST", "CIFAR-10"]
        if self.dataset_name not in valid:
            raise ValueError(f"Dataset must be one of {valid}, got {dataset_name}")

        self.num_classes = 10
        self.input_channels = 1 if self.dataset_name in ["MNIST", "F-MNIST"] else 3
        self.input_size = 28 if self.dataset_name in ["MNIST", "F-MNIST"] else 32
        # The GPU-resident path materialises data once, so train-time augmentation
        # would be frozen; disabled by default (deterministic transforms).
        self.train_augment = False

    def _transform(self, train: bool) -> transforms.Compose:
        if self.dataset_name in ["MNIST", "F-MNIST"]:
            return transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.5,), (0.5,)),
            ])
        # CIFAR-10
        if train and self.train_augment:
            return transforms.Compose([
                transforms.RandomCrop(32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
        return transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
        ])

    def _load(self, train: bool, download: bool) -> Dataset:
        tf = self._transform(train)
        if self.dataset_name == "MNIST":
            return datasets.MNIST(self.data_path, train=train, download=download, transform=tf)
        if self.dataset_name == "F-MNIST":
            return datasets.FashionMNIST(self.data_path, train=train, download=download, transform=tf)
        return datasets.CIFAR10(self.data_path, train=train, download=download, transform=tf)

    def load_data(self, download: bool = True) -> Tuple[Dataset, Dataset]:
        return self._load(True, download), self._load(False, download)

    def info(self) -> dict:
        return {
            "name": self.dataset_name,
            "num_classes": self.num_classes,
            "input_channels": self.input_channels,
            "input_size": self.input_size,
        }
