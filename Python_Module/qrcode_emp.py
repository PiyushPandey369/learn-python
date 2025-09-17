import qrcode as qr

# Create QR code
img = qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg&t=4388s")

# Save the QR code as an image file
img.save("yt_qr.png")

# Optionally display the QR code
img.show()
