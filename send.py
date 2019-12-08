from digitalio import DigitalInOut
import adafruit_rfm9x
import board
import busio
import sys
import time

CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23

if len(sys.argv) > 1:
    content = bytes(sys.argv[1], "utf-8")
    rfm9x.send(content)
else:
    print("Usage: python3 send.py MESSAGE")
