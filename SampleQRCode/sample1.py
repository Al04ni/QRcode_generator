import qrcode
import os

#creating the qrcode object with larger size and higher error handling
qr = qrcode.QRCode(version=3, box_size=20, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)

# Define the data to be encoded in the QR code
data = "https://your_link_here.com" #Feel free to add text or a link

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")

#Defining the folder to save the images
output_folder =os.path.join(os.getcwd(), "./Samples") 
os.makedirs(output_folder, exist_ok=True)

#Defining the file name &full path to save the file
file_name = "nameit.png"
file_path = os.path.join(output_folder, file_name)

# Save the QR code image
img.save(file_path)

print(f"QR code {file_name} saved in {file_path}")

