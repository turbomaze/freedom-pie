from digitalio import DigitalInOut
import adafruit_rfm9x
import adafruit_ssd1306
import board
import busio
import time

# Display
i2c = busio.I2C(board.SCL, board.SDA)
reset_pin = DigitalInOut(board.D4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
display.fill(0)
display.show()

# Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
previous_packet = None

while True:
    packet = None
    display.fill(0)
    display.text('FREEDOM PIE', 35, 0, 1)

    packet = rfm9x.receive()
    if packet is None:
        display.show()
        display.text('- Waiting for PKT -', 15, 20, 1)
    else:
        display.fill(0)
        previous_packet = packet
        content = str(previous_packet, "utf-8")
        display.text('RX: ', 0, 0, 1)
        display.text(content, 25, 0, 1)
        time.sleep(1)

    display.show()
    time.sleep(0.1)
