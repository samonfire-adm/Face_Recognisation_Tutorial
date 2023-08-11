import cv2


capture = cv2.VideoCapture(0)
capture.set(3,1920)
capture.set(4,1080)

bg = cv2.imread('Source/bg.png')

while True:
    success, img = capture.read()
    # cv2.imshow("Face Attadance ", img)
    bg[162:162+480, 55:55+640] = img
    cv2.imshow("Main", bg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
capture.release()
cv2.destroyAllWindows()




