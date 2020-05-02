import qrcode
def Generate_QRcode(Homework_Assignment):
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 15,
        border = 5)
    qr.add_data(Homework_Assignment)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('Student.png')

    
Homework_Assignment = str(input("Homework: "))
Generate_QRcode(Homework_Assignment)
