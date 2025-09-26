import photo as ph
cam= ph.photograph()
hand= ph.handDetector()

while True:
    frame= cam.camera()
    output= hand.findHands(frame)
    hand.findPosition(output)
    cam.show(output)