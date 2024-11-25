# utility functions, logging 
import matplotlib.pyplot as plt
import numpy as np

def plot_images_with_masks(images, masks, categories, category_names):
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(10, 10))
    for i, (image_path, mask_path, category) in enumerate(zip(images, masks, categories)):
        image, mask = load_image_and_mask(image_path, mask_path)
        row, col = divmod(i, 4)
        ax_image = axes[0, col]
        ax_image.imshow(image)
        ax_image.axis('off')
        ax_image.set_title(f"Category: {category_names[category]}")
        ax_mask = axes[1, col]
        ax_mask.imshow(image)
        ax_mask.imshow(mask, cmap='jet', alpha=0.55)
        ax_mask.axis('off')
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.tight_layout()
    plt.show()

def visualize_batch(images, masks):
    batch_size = len(images)
    fig, axes = plt.subplots(batch_size, 2, figsize=(10, batch_size * 5))
    for i in range(batch_size):
        ax_image = axes[i, 0]
        ax_image.imshow(images[i])
        ax_image.axis('off')
        ax_mask = axes[i, 1]
        ax_mask.imshow(masks[i], cmap='gray')
        ax_mask.axis('off')
    plt.tight_layout()
    plt.show()
