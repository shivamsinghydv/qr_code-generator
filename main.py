import qrcode
# type(qrcode.make('hi'))  # qrcode.image.pil.PilImage

def main(string):
    qrcode.make(string).save("qr_code.png")

if __name__ == '__main__':
    string = input("Enter the string to be encoded: ")
    main(string)
