#Importing Libraries
import cv2 as cv
import os

# Initializing Variables
low_H = 1
low_S = 1
low_V = 1
high_H = 180
high_S = 255
high_V = 99
low_mid_V = 49
high_mid_V = 51

low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'
low_mid_V_name = "LOW MID V"
high_mid_V_name = "HIGH MID V"

# Finding Current Path
path = os.getcwd()
data_dir = path+'/InputFile/'
dataset = os.listdir(data_dir)
c = 1

print("Visuliazing only dominant colors for approx 900 Photos")

# Creating Output Images
for val in dataset:
    
    print("Creating ",c,"Image")
    c+= 1
    
    image = cv.imread(data_dir+val)
    if image is None:
        break
    image_HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    mask1 = cv.inRange(image_HSV, (low_H, low_S, low_V), (high_H, high_S, low_mid_V))
    mask2 = cv.inRange(image_HSV, (low_H, low_S, high_mid_V), (high_H, high_S, high_V))

    mask = cv.bitwise_or(mask1, mask2)
    target = cv.bitwise_and(image,image, mask=mask)    

    cv.imwrite(path+'/OutputFile/'+val,target)
print("Check the Output Folder named as Output File")
print("Thank You")
