from stegano import lsb

message = 'print("Hello World")'

image = lsb.hide(image=r'image.png', message=message)

image.save(r"E:\python-programs\dropper\workspace\eimage.png")