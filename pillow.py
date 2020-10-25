import PIL
from PIL import Image

#mywidth = 3840
#myheight = 2160

img=Image.open('wallpaper.jpg')
img=img.resize((768,768),PIL.Image.ANTIALIAS)
img.save('pillow.jpg')
img.show()