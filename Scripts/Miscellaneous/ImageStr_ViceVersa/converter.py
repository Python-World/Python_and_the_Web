import base64
from PIL import Image
import io
from skimage.metrics import structural_similarity
import cv2

im_path = "test.jpg"
# Convert to base64 encoding
print("Encoding....")
with open(im_path, "rb") as imageFile:
    base64_encoding = base64.b64encode(imageFile.read())
    # print(base64_encoding)

print("Decoding and writing to image...")
# Write to the image
f = io.BytesIO(base64.b64decode(base64_encoding))
pilimage = Image.open(f)
pilimage.save("image_from_encoding.jpg")
print("Image saved!")

# Let's check for the structural similarity between original and generated image.
original = cv2.imread("test.jpg", 0)
generated = cv2.imread("image_from_encoding.jpg", 0)
# Similarity index should be greater than 0.90
similarity_index = structural_similarity(original, generated)
print(f"Similarity index is {similarity_index}")
