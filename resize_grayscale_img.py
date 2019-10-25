import cv2
import os

for i in os.listdir('Z:/Study Material BITS/3-1/AI/AI Project/bing/'):
    img = cv2.imread('Z:/Study Material BITS/3-1/AI/AI Project/bing/'+str(i),cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img,(720,540))
    cv2.imwrite('Z:/Study Material BITS/3-1/AI/AI Project/bing2/'+str(i),resized)