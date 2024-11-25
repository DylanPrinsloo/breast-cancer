# data cleaning
import numpy as np
import json
import cv2
import os
import matplotlib.pyplot as plt
from PIL import Image
'''
def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def parse_json(data):
    categories = {cat['id']: cat['name'] for cat in data['categories']}
    images = {img['id']: img['file_name'] for img in data['images']}
    return categories, images

def load_image_and_mask(image_path, mask_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    return image, mask

def load_image_and_mask_pil(image_path, mask_path, target_size=(256, 256)):
    image = Image.open(image_path).convert('RGB')
    mask = Image.open(mask_path).convert('L')
    image = image.resize(target_size, Image.Resampling.LANCZOS)
    mask = mask.resize(target_size, Image.Resampling.LANCZOS)
    image = np.array(image)
    mask = np.array(mask)
    return image, mask
'''
# learning 2024/11/25

def load_images_from_folder(folder_path):
    images = []
    labels = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Add other image formats if needed
            label = int(filename.split('_')[0])  # Assuming filenames are in the format '0_image.jpg' or '1_image.png'
            img_path = os.path.join(folder_path, filename)
            image = cv2.imread(img_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            images.append(image)
            labels.append(label)
    return np.array(images), np.array(labels)

# Example usage
folder_path = 'path/to/your/folder'
images, labels = load_images_from_folder(folder_path)
