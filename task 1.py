#import matplotlib.pyplot as plt
import numpy as np
figarr = []
arr = []
midle = 0

#figure1.txt, figure2.txt, figure3.txt etc......
print("input figure number: ")
number=input()

def widthmm(image, pixmm):
	maxs = 0
	mins = image.shape[1]
    
	for y in range(image.shape[0]):
		for x in range(image.shape[1]):
			if(image[y, x] == 1):
				if(x > maxs):
					maxs = x
				if(x < mins):
					mins = x
    
	return(float(maxs-mins+1) / pixmm); 


figopen = open("figure"+number+".txt","r").readlines()
#print(figopen)
figfloat = float(figopen.pop(0))
figopen.pop(0)

for i in figopen:
	arr.append(i.split())
    
for i in arr:
	arri = []
	for j in i:
		arri.append(int(j))
	figarr.append(arri.copy())

image = np.array(figarr)
print("Nominal resolution(mm/pixel)= ", widthmm(image, figfloat))