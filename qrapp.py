import qrcode

sitioweb = input("Añade aquí la URL: ")
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(sitioweb)
qr.make(fit=True)

imagen = qr.make_image(fill_color="black", back_color="white")
imagen.save(f"{input()}.png")
