from four_point_transform import four_point_transform
import cv2
import imutils
import numpy as np
#from skimage.filters import threshold_local
#from scipy.ndimage import morphology, label
import pytesseract
from random import randint
from PIL import Image, ImageOps, ImageDraw
import re
image = cv2.imread("good_test.jpg")
pillow = Image.fromarray(image)
text = pytesseract.image_to_string(pillow)
#print(text)
regex = re.compile('[^a-zA-Z]')
text = [str.strip() for str in text.splitlines()]
print(text)
text = [x for x in text if (any(c.isalpha() for c in x) and any(c.isdigit() for c in x))]
print(text)
def getCost(s):
    x = -1
    for t in s.split():
        try:
            x = float(t[1:] if t[0] == "$" else t)
        except ValueError:
            pass
    if x>0:
        if int(x) == x and x%10!=0:
            x = x/100
    return x

totIndex = -1

for i in range(len(text)):
    if 'subtotal' in text[i].lower():
        totIndex = i
        break
        #print(text[i].lower())
print(totIndex)
print(text[totIndex])
print(text[0:totIndex+1])
text = text[0:totIndex+1]
text.reverse()
print(text)
totCost = getCost(text[0])
print(totCost)
items = []
prices = []
for i in range(1, len(text)):
    x = getCost(text[i])
    if x>=0:
        totCost-=x
        if totCost<0:
            break
        prices.append(x)
        items.append(text[i][0:re.search("\d", text[i]).start()])

'''def getCost(string):
    x = -1
    for t in s.split():
        try:
            x = float(t)
        except ValueError:
            pass
    if x>0:
        if int(x) == x and x%10!=0:
            x = x/100
    return x
'''
for i in range(len(items)):
    items[i]=regex.sub('', items[i])

print(items)
print(prices)
