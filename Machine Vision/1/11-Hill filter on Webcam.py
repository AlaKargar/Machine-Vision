import photo as ph
x= ph.funcam()
x.filter_record(filter= 'hill', stopkey= 'q', outputname= 'output.avi')
x.hiddencam(stopkey= 'q', snaptime= 6)
x.exitcam()