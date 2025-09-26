import photo as ph
cam= ph.photograph()
faces= ph.Facetracker()

while True:
    camera= cam.camera()
    try:
        x= faces.faceRejaction(camera)
    except:
        x= camera
    exitkey= cam.show(x)
    