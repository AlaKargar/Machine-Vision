import photo as ph
x= ph.photograph()
fc= ph.Facetracker()

while True:
    frame= x.camera()
    frame= x.see_eye(frame)
    output= fc.Facefinder(frame)
    x.show(frame)
    