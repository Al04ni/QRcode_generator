from datetime import datetime
import qrcode
import os

#Defining the content you want on your vCard
vcard = f"""
VERSION:3.0
N:Niyonsenga;Albert;;;
FN:Albert Niyonsenga
BDAY:19831014
ADR;type=HOME:;;;Kicukiro;Kigali;KG378KK;Rwanda
TEL;type=CELL:123456785
EMAIL;type=PERSONAL,INTERNET:username@gmail.com
TITLE:Software Engineer
EMAIL;type=WORK,INTERNET:username@gmail.com
REV:{datetime.now()}
"""

#Then let's go for the creation of the QRCode
def create_qr_code(output_path):
    qr_object =  qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr_object.add_data(vcard)
    qr_object.make(fit=True)
    
    output_folder =os.path.join(os.getcwd(), "Samples")
    file_name = "vcard_sample1.png"
    file_path = os.path.join(output_folder, file_name)
    img = qr_object.make_image(fill_color='black', back_color='white')
    img.save(file_path)
    
    
if __name__ == "__main__":
    output_folder =os.path.join(os.getcwd(), "Samples")
    file_name = "qrcode_sample1.png"
    file_path = os.path.join(output_folder, file_name)
    create_qr_code(file_path)

