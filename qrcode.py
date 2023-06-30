import pyqrcode 
from pyqrcode import QRCode 
  
#Prompt user for url
st = input("Enter URL to be converted to QR Code:\n")

# Generate QR code 
url = pyqrcode.create(st) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 