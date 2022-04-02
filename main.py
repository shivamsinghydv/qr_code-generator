import qrcode
img = qrcode.make('https://www.shivamsinghydv.cf')
type(img)  # qrcode.image.pil.PilImage
img.save("qr_code.png")
