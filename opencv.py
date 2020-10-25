import cv2

img = cv2.imread("wallpaper.jpg")
#print(img.shape[0])height
#print(img.shape[1])width

img_scaled = cv2.resize (img,None,fx=0.75,fy=0.75)
cv2.imshow('',img_scaled)

cv2.waitkey(0)
cv2.destroyAllWindows()
