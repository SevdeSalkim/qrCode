import segno

data = "https://youtu.be/DslHQto2V7I?si=I_CnnE3NCFwVkahi"

qrcode = segno.make_qr(data)
qrcode.save("qrcode.png", light=(255 ,13,0), dark=(255,255,255),scale=10)