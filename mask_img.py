import cv2
import numpy as np
import os , sys
img = cv2.imread('Z:/Study Material BITS/3-1/AI/AI Project/2.jpg',1)
print(img.shape)

print(img[2,3])

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        if(np.all(img[x,y]==[0,0,254])):
            img[x,y]=[0,0,0]
            print("WORKING!")
        else:
            img[x,y]=[255,255,255]
            
            
            
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
           
cv2.imwrite("Z:/Study Material BITS/3-1/AI/AI Project/MASK_BOUNDARY.png",img)
# =============================================================================
# =============================================================================
# # # =============================================================================
# # 
# # #             
# # # =============================================================================
# # for x in range(img.shape[0]):
# #     for y in range(img.shape[1]):
# #         if(np.all(img[x,y]==[0,0,255])):
# #             img[x,y]=[255,255,255]
# #             print("WORKING! yayyy")
# #         else:
# #             img[x,y]=[0,0,0]   
# #             print("NOOOO")
# # 
# # for x in range(0,540,1):
# #     for y in range(0,686,1):
# #        # print(x,y)
# #         #file.write(str(img[x,y,0].tolist())
# #         #np.savetxt(file, img[x,y], fmt="%d")
# #         #print(img[x,y])
# #         if img[x,y] is [0,0,255]:            
# #             img[x,y] = [0,0,0]
# #             print("going")
# #             
# # print(img.shape)
# # #file = open('temp1.txt', 'w')   
# # for x in range(0,540):
# #     for y in range(0,686):
# #        # print(x,y)
# #         #file.write(str(img[x,y,0].tolist())
# #         #np.savetxt(file, img[x,y], fmt="%d")
# #         #print(img[x,y])
# #         if img[x,y,0] == 255 and img[x,y,1] == 0 and img[x,y,2] == 0:            
# #             img[x,y,0] = 0
# #             img[x,y,1] = 0
# #             img[x,y,2] = 0
# #             print("going")
# # 
# # # =============================================================================
# # #         else:
# # #             img[x,y,0] = 255
# # #             img[x,y,1] = 255
# # #             img[x,y,2] = 255
# # # =============================================================================
# #             #print("nope")
# # #file.close()      
# # cv2.imwrite("MASK_BOUNDARY.png",img)
# # 
# # 
# # 
# # import cv2
# # 
# # img=cv2.imread("suzuki-baleno-hero1_new.jpg")
# # height, width, channels = img.shape
# # print(height)
# # 
# # white = [255,255,255]
# # black = [0,0,0]
# # 
# # for x in range(0,width):
# #     for y in range(0,height):
# #         channels_xy = img[y,x]
# #         #print("hiiii",channels_xy,"yahooooo")
# #         if all(channels_xy == white):    
# #             img[y,x] = black
# # 
# #         elif all(channels_xy == black):
# #             img[y,x] = white
# # 
# # cv2.imshow('img',img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # 
# # import cv2
# # 
# # 
# # img=cv2.imread("suzuki-baleno-hero1_new.jpg")
# # img=cv2.resize(img, (300,300))
# # height, width, channels = img.shape
# # 
# # print(height,width,channels)
# # 
# # for x in range(0,width):
# #     for y in range(0,height):
# #         if img[x,y,0] == 255 and img[x,y,1] == 255 and img[x,y,2] == 255:            
# #             img[x,y,0] = 0
# #             img[x,y,1] = 0
# #             img[x,y,2] = 0
# #             print("HEllo")
# # 
# #         elif img[x,y,0] == 0 and img[x,y,1] == 0 and img[x,y,2] == 0:
# #             img[x,y,0] = 255
# #             img[x,y,1] = 255
# #             img[x,y,2] = 255
# # 
# # 
# # cv2.imshow('img',img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# =============================================================================
# 
# =============================================================================











