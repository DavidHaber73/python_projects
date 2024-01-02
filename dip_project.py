import numpy as np
import matplotlib.pyplot as plt

def shrink_image(original_image, D):
    # Get dimensions of the original image
    N, M = original_image.shape

    # Calculate dimensions of the new image
    N_prime = N // D
    M_prime = M // D

    # Initialize the new image with zeros
    new_image = np.zeros((N_prime, M_prime))

    # Replicate and fill in the gaps
    for x_prime in range(N_prime):
        for y_prime in range(M_prime):
            x = x_prime * D
            y = y_prime * D
            new_image[x_prime, y_prime] = original_image[x, y]

    return new_image

# Example usage:
original_image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
D = 2

shrunk_image = shrink_image(original_image, D)

# Display original and shrunk images
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray', interpolation='nearest')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(shrunk_image, cmap='gray', interpolation='nearest')
plt.title('Shrunk Image')

plt.show()

from PIL import Image

def shrink_image(input_path, output_path, scale_factor):
    # Open the image file
    image = Image.open(input_path)
    imga=np.asarray(image)
    # Calculate new dimensions
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Save the resized image to the output file
    rimga=np.asarray(resized_image)
    resized_image.save(output_path)

    print(imga.shape, rimga.shape)
    print(rimga)


# Example usage
input_image_path = "/home/davidhaber/Pictures/tree.tif"
output_image_path = "/home/davidhaber/Pictures/output.png"
scale_factor = 0.5  # Adjust this factor according to your needs

shrink_image(input_image_path, output_image_path, scale_factor)
plt.imshow(plt.imread(output_image_path))

