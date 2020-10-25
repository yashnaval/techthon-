from PIL import Image

im = Image.open("project.jpg")
im.thumbnail((768,768),Image.ANTIALIAS)
im.save("Thumbnail2.jpg","JPEG")
im.show()