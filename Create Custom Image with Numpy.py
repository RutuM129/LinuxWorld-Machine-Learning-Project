import numpy as np
import matplotlib.pyplot as plt

def create_custom_image():
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    image[25:75, 25:75] = [255, 0, 0]  # Red square
    plt.imshow(image)
    plt.axis('off')
    plt.show()