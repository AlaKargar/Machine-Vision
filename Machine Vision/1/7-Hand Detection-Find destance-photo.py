import photo as ph
import cv2
cam= ph.photograph()
hd= ph.handDetector()

cap= cv2.VideoCapture(0)

while True:
    success, img= cap.read()
    if not success:
        break
    
    img= hd.findHands(img)
    lmlist, _= hd.findPosition(img)
    if len(lmlist) >= 21:
        distance, _= hd.findDistance(8, 19, img)
        print(f"Distance between teo fingers: {distance}")
        cv2.imshow('W', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()