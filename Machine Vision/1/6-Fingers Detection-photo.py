import photo as ph
cam= ph.photograph()
hd= ph.handDetector()

while True:
    frame = cam.camera()
    output = hd.findHands(frame)
    lmList, _ = hd.findPosition(output)
    fingers = hd.fingersUp(lmList)  # Check which fingers are up
    print(f"Fingers Up: {fingers}")
    cam.show(output)



# while True:
#     frame= cam.camera()
#     output= hand.findHands(frame)
#     lmlist=hand.findPosition(output)
#     fingers= hand.fingersUp(lmlist)
#     print(f"Fingers Up: {fingers}")
#     cam.show(output)