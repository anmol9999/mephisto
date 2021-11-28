import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('face_cascade.xml')

while True:

    ret ,frame = cap.read()

    faces = classifier.detectMultiScale(frame)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),  (0,0,255), 2)
        
    # print (frame)
    cv2.imshow("reading webcam", frame)

    if cv2.waitKey(100) & 0xFF ==ord('q'):      
        break
    


cv2.destroyAllWindows()

cap.release()