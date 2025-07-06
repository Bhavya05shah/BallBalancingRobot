import cv2 as cv

ball_img = cv.imread('/Users/bhavyashah/Desktop/OpenCV/Ball_Balancing_Ball.jpg')
gray = cv.cvtColor(ball_img , cv.COLOR_BGR2GRAY)
ret , thresh = cv.threshold(gray , 145, 255 , cv.THRESH_BINARY)
contours , heirarchies = cv.findContours(thresh , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)

for i,contour in enumerate(contours):
  if i==0:
    continue
  epsilon = 0.01*cv.arcLength(contour,True)
  approx = cv.approxPolyDP(contour , epsilon , True)

  cv.drawContours(thresh , contour, 0 , (0,0,0), 4)

  x,y,w,h = cv.boundingRect(approx)
  x_mid = int(x+w/3)
  y_mid = int(y+h/1.5)

  coords = (x_mid , y_mid)
  colour = (0,0,0)
  font = cv.FONT_HERSHEY_DUPLEX

  if len(approx) > 15:
    cv.putText(thresh , "Circle" , coords , font , 1,colour , 1)
  
cv.imshow("window" , thresh)
cv.waitKey(0)