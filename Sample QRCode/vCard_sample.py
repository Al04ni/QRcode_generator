import qrcode
import os

#Defining the content you want on your vCard
vcard = f"""
Your content goes here
----  ----  ----  
"""
# The `f` before the triple quotes `"""` in the `vcard` variable definition denotes an f-string in
# Python. This allows you to embed expressions inside curly braces `{}` within the string. In this
# case, the f-string is used to format the multi-line string with the ASCII art for the vCard.


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
    
    img = qr_object.make_image(fill_color='black', back_color='white')
    img.save(file_path)
    
    
if __name__ == "__main__":
    output_folder =os.path.join(os.getcwd(), "Samples")
    file_name = "vcard1.png"
    file_path = os.path.join(output_folder, file_name)
    create_qr_code(file_path)

