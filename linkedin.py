import qrcode

# Define the LinkedIn profile link
linkedin_link = "https://www.linkedin.com/in/rohit-panchal-7585a7205/"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

# Add the LinkedIn link to the QR code
qr.add_data(linkedin_link)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("linkedin_qr.png")

print("QR code generated and saved as linkedin_qr.png")
