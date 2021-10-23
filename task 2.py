#import matplotlib.pyplot as plt
import numpy as np

def ImageRead(file):
	imopen = open(file, "r").readlines()
	imfloat = float(imopen.pop(0))
	imopen.pop(0)
	arr = []
    
	for i in imopen:
		arr.append(i.split())
	barr = []
    
	for i in arr:
		collab = []
		for j in i:
			collab.append(int(j))
		barr.append(collab.copy())

	image = np.array(barr)
	return image

def Point(image):
	ymin = image.shape[0]
	xmin = image.shape[1]
    
	ymax = 0
	xmax = 0

	for y in range(image.shape[0]):
		for x in range(image.shape[1]):
			if(image[y, x] == 1):
				if(y < ymin):
					ymin = y
				elif(x < xmin):
					xmin = x
				elif(y > ymax):
					ymax = y
				elif(x > xmax):
					xmax = x
                
	return [xmin, ymin]


print("Choose 2 txt files in folder(img1/img2):")
inp1=input()
inp2=input()

im1 = ImageRead(inp1 + ".txt")
im2 = ImageRead(inp2 + ".txt")

Pone = Point(im1)
Ptwo = Point(im2)

x = Pone[0] - Ptwo[0]
y = Pone[1] - Ptwo[1]

print("Offset between images(x/y) = " + str(x) + " " + str(y))

	