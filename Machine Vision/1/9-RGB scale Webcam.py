import photo as ph
x= ph.photograph()

while True:
    frame= x.camera()
    k= x.show(frame, windowname= 'wincam', f= 'rgb')
    if k== ord('q'):
        break