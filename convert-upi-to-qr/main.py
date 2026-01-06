import qrcode

upi = input("Please enter your upi id...!\n")
filename = input("Filename you want to save in\n")
if not(filename.endswith(".png")):
    filename = filename+".png"

img = qrcode.make(upi)
img.save(filename)