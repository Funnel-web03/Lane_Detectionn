# Lane_Detectionn
Lane detection using OpenCV
Steps :-
1) Adjust Threshold value for canny egde detection once you set with ooptimal values press esc
2) Now origional captured frame and threshold value pass to process function
3) Convert Color image to gray scale image
4) Apply Canny edge detecion on original imgae
5) Define region of interest usiing cordinates and perform masking on unwanted area
6) using Houghline Transform (Probabalistic) define lines
7) Draw lines on same size black image
8) Perform weighted addition of original frame and line


wholla.....You did the lane detection successfully using openCV

make sure to adjust Regionn Of Interest Accoring to your input video
Once you execute the code you will get black image that is to set optimal threshld vlaues using trackbar
press esc once you set optimal threshold values
