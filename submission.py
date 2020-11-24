import pyotp # version 2.3.0
import pyqrcode


# generate QR code
def generateqr(data):
    qr = pyqrcode.create(data)
    qr.png('abc.png',scale=8)

link = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='tester@google.com', issuer_name='Secure App')

generateqr(link)