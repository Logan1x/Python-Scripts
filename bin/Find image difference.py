# importing dependecies
from PIL import Image ,ImageChops
img1=Image.open("Image Difference/img1.jpg")
img2=Image.open("Image Difference/img2.jpg") 

#returns the new image with pixel-by-pixel difference between the two images
newImage=ImageChops.difference(img1,img2) 
if newImage.getbbox():
        newImage.show()
