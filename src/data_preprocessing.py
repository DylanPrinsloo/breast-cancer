# data cleaning
import numpy as np
import json
import cv2
import os
import matplotlib.pyplot as plt
from PIL import Image

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
