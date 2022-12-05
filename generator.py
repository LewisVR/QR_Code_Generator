import qrcode  # => QR Code kütüphanesi

qr_image = qrcode.make('https://github.com/LewisVR') 
qr_image.save('Github.png')
