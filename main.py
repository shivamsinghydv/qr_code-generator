import qrcode
type(qrcode.make('pass your string here'))  # qrcode.image.pil.PilImage
qrcode.make('pass your string here').save("qr_code.png")
