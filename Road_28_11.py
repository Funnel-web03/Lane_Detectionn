import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap = cv.VideoCapture('road 1.mp4')
x=1
thresh=[]
def process(image,min_thresh,max_thresh) : 
   
    canny_img = cv.cvtColor(image,cv.COLOR_BGR2GRAY)    #convetring_color_to_gray   
    canny1_img = cv.Canny(canny_img,thresh[0],thresh[1])    #Edge_detection

    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices=[(0,600),(560,300),(686,300),(1030,650)] #change_region_of_interest_according_to_video
    def region_of_interest(img,vertices):
        mask = np.zeros_like(img)
        #channel_count = img.shape[2]
        match_mask_color = 255
        cv.fillPoly(mask,vertices,match_mask_color)
        masked_image = cv.bitwise_and(img,mask)
        return masked_image

    def draw_line(img1,lines1):
        img = np.copy(img1)
        blank = np.zeros((img1.shape[0],img1.shape[1],3),dtype=np.uint8)
        for line in lines1:
            for x1,y1,x2,y2 in line:
                cv.line(blank,(x1,y1),(x2,y2),(0,255,0),2)
        img1 = cv.addWeighted(img1,0.8,blank,1,0.0)
        return img1
    croped_img = region_of_interest(canny1_img,np.array([region_of_interest_vertices],np.int32))
    lines = cv.HoughLinesP(croped_img,3,np.pi/60,threshold=70,
                       lines=np.array([]),minLineLength=80,maxLineGap=20)
    #change_some_parameters_for_better_result
    image_with_lines = draw_line(image,lines)
    return image_with_lines

while (cap.isOpened()) :
    ret,frame = cap.read()
    frame=cv.resize(frame,(1280,720))
    if x == 1:
                #all_is_done_to_findout_optimal_threshold_range
                #press esc key once you set the proper values
                x=0
                frame1=frame.copy()
                frame1=cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
                def nothing(x):
                    pass
                cv.namedWindow('Adjust')
                cv.createTrackbar('Min Thresh','Adjust',40,255,nothing)
                cv.createTrackbar('Max Thresh','Adjust',240,255,nothing)
                while (True):
                    x = cv.getTrackbarPos('Min Thresh','Adjust')
                    y = cv.getTrackbarPos('Max Thresh','Adjust')
                    thresh.append(x)
                    thresh.append(y)
                    canny_img = cv.Canny(frame1,x,y)
                    cv.imshow('canny',canny_img)
                    k = cv.waitKey(10)
                    if k==27:
                         break
                cv.destroyAllWindows()
    frame = process(frame,thresh[0],thresh[1]) #sending frame for processing
    cv.imshow('Frame',frame)
    k = cv.waitKey(2) #frames loading at speed of frame/ 2 ms 
    if k == 27:    #if you wanna stop prior press esc
         break
cap.release()
cv.destroyAllWindows()