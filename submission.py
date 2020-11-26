import pyotp # version 2.3.0
import pyqrcode
import sys
from pyzbar.pyzbar import decode
import cv2
from random import randrange
# from PIL import Image
from time import sleep

# generate QR code
def generateqr(data,fname):
    qr = pyqrcode.create(data)
    qr.png(fname +'.png',scale=8)


# main
if __name__ == "__main__":

    if sys.argv[1] == "--generate-qr": # generate QR

        fname = input("What you would like the QR png name to be, much without .png: ")
        email = input("What is your email, without the @google.com: ")

        # link for generating the TOTP
        # having the same TOTP will result in the same key
        link = pyotp.totp.TOTP(pyotp.random_base32()).provisioning_uri(name=email, issuer_name='Secure App')
        print (link)
        generateqr(link,fname)

    if sys.argv[1] == "--get-otp": # number of the QR
        fname = input("Name of png, without .png: ")

        d = decode(cv2.imread(fname + '.png')) # data in b''
        data = d[0].data.decode('utf-8') # converts it to utf-8
        secret = data[data.find('secret=') + len('secret='):data.find('secret=') + len('secret=') + 16 ] # secret 

        # print(d)
        totp = pyotp.TOTP(secret)
        print("Current OTP:", totp.now())


