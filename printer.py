# from escpos import *
""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T88IV) """
"""
p = printer.Usb(0x04b8,0x0202)
# Print text
p.text("Hello World\n")
# Print image
p.image("logo.gif")
# Print QR Code
p.qr("You can readme from your smartphone")
# Print barcode
p.barcode('1324354657687','EAN13',64,2,'','')
# Cut paper
p.cut()
"""

from escpos.printer import Network
#kitchen = Network("192.168.1.240") #Printer IP Address
kitchen = Network("127.0.0.1") #Printer IP Address
kitchen.text("Hello World\n")
# kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
kitchen.cut()
