import photo as ph
x = ph.photograph()
while True:
    frame = x.camera()
    frame = x.cvdata(p=frame , data='haarcascade_eye.xml')
    x.show(frame)
