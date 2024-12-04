import os
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import matplotlib.pyplot as plt
import random

def process_images_from_directory(directory, label, target_size=(64, 64)):
    """
    Load, resize, and convert images into numpy arrays.

    Args:
        directory (str): Path to the image directory.
        label (int): Label for the class (1 for parasitized, 0 for uninfected).
        target_size (tuple): Target size for resizing images.

    Returns:
        images (list): List of numpy arrays for images.
        labels (list): Corresponding labels.
    """
    images = []
    labels = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            img_path = os.path.join(directory, filename)
            img = load_img(img_path, target_size=target_size)
            img_array = img_to_array(img)
            images.append(img_array)
            labels.append(label)
    return np.array(images), np.array(labels)

def plot_random_images(directory, label, num_images=4, target_size=(64, 64)):
    """
    Visualizes a random set of images from the given directory.

    Args:
        directory (str): Path to the directory containing images.
        label (str): Class label (Parasitized/Uninfected).
        num_images (int): Number of random images to display.
        target_size (tuple): Target size for resizing images.
    """
    plt.figure(figsize=(10, 5))
    plt.suptitle(f"Sample {label} Images", fontsize=16)

    random_images = random.sample(os.listdir(directory), num_images)
    for i, img_name in enumerate(random_images):
        img_path = os.path.join(directory, img_name)
        img = load_img(img_path, target_size=target_size)
        plt.subplot(1, num_images, i + 1)
        plt.imshow(img)
        plt.axis('off')