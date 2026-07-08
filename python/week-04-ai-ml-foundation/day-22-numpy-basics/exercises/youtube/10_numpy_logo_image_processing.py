# NumPy Logo Image Processing
# Practice: Load an image as a NumPy array and create a dark/inverted variant.

import urllib.request

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# Define the image URL.
numpy_logo_url = "https://img.icons8.com/color/1200/numpy.jpg"

# Add a standard User-Agent header to avoid a 406 security block from the image host.
request = urllib.request.Request(
    numpy_logo_url,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
)

# Download the image data and convert it into a NumPy array.
with urllib.request.urlopen(request) as response:
    numpy_logo = np.array(Image.open(response).convert("RGB"))

# Set up the plotting area.
plt.figure(figsize=(10, 5))

# Plot 1: Original logo.
plt.subplot(121)
plt.imshow(numpy_logo)
plt.title("NumPy Logo")
plt.grid(False)
plt.axis("off")

# Plot 2: Dark variant by inverting RGB values.
# For normal uint8 images, colors range from 0 to 255, so 255 - value inverts them.
numpy_dark_logo = 255 - numpy_logo

plt.subplot(122)
plt.imshow(numpy_dark_logo)
plt.title("NumPy Dark Logo")
plt.grid(False)
plt.axis("off")

plt.show()
