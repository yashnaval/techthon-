import  PIL
from PIL import Image
im = Image.open("wallpaper.jpg")
new_height = 512
new_width = int(new_height / im.height * im.width)
im = im.resize((new_width,new_height))
im.save('pillow2.jpg')
im.show()