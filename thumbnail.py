
from PIL import Image

im = Image.open("wallpaper.jpg")
#im.show()

from PIL import Image
import glob, os
size = 1024,1024
for infile in glob.glob("project.jpg"):
    file,ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail","JPEG")
    im.show()