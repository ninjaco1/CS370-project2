import pyotp # version 2.3.0
import pyqrcode
import sys
from time import sleep



# generate QR code
def generateqr(data):
    qr = pyqrcode.create(data)
    qr.png('abca.png',scale=8)


# main
if __name__ == "__main__":
    if sys.argv[1] == "--generate-qr": # generate QR
        # link for generating the TOTP
        # having the same TOTP will result in the same key
        link = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='testers@google.com', issuer_name='Secure App')
        print link
        generateqr(link)

    if sys.argv[1] == "--get-otp": # number of the QR
        totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
        print("Current OTP:", totp.now())