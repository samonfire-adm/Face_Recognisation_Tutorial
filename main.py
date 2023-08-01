import cv2


capture = cv2.VideoCapture(0)
capture.set(3,1920)
capture.set(4,1080)


while True:
    success, img = capture.read()
    cv2.imshow("Face Attadance ", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
capture.release()
cv2.destroyAllWindows()




