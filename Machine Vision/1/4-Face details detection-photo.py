
import photo as ph
cam= ph.photograph()
fc= ph.Facetracker()

while True:
    frame= cam.camera()
    output= fc.Facefinder(frame)
    cam.show(output)
    
   



    