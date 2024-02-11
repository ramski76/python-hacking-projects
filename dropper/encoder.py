from stegano import lsb

message = 'print("Hello World")'

image = lsb.hide(image=r'/path/to/normal/image', message=message)

image.save(r"/path/to/save/encoded/image")
