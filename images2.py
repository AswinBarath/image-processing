from PIL import Image, ImageFilter
img = Image.open('./astro.jpg')

new_img = img.resize((400, 400))
new_img.save("thumbnail.jpg")

# Thumbnail function Maintains aspect ratio
# Modifies existing image
img.thumbnail((400, 400))
img.save("thumbnail2.jpg")

