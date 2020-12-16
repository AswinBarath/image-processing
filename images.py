from PIL import Image, ImageFilter
img = Image.open('./Pokedex/pikachu.jpg')

# Image Filters
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", 'png')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", 'png')
# filtered_img.show()

# Conversion
filtered_img = img.convert('L')
filtered_img.save("grey.png", "png")

# Rotate
crooked = filtered_img.rotate(90)
crooked.save("rotate1.png", "png")
crooked = filtered_img.rotate(180)
crooked.save("rotate2.png", "png")

# Resize
resize = filtered_img.resize((300, 300))
resize.save("resized.png", "png")

# Crop
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("cropped.png", "png")
