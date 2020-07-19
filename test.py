import cv2

cap = cv2.VideoCapture(0)
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")
pred=[]
while(True):
    
    check,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5,minSize=(1,1),flags=cv2.CASCADE_SCALE_IMAGE)
    vertices=[]
    for(x,y,w,h) in faces:
        pred_id,mm=clf.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)
        cv2.putText(frame, str(pred_id), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 1, cv2.LINE_AA)
        vertices=[x,y,x+w,y+h]
    pred_id,mm=clf.predict(gray[y:y+h,x:x+w])
    cv2.imshow('frame',frame)
    
    
    pred.append(pred_id)
    
        
    if cv2.waitKey(1) & 0xFF==ord('1'):
        break

cap.release()  
cv2.destroyAllWindows()