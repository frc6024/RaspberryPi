import sys
from neopixel import *

LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

#Off = 0
#Red = 1
#Green = 2
#Blue = 3

print(sys.argv)
if len(sys.argv) > 1:
    num = int(sys.argv[1])
    r = 255 if num == 1 else 0
    g = 255 if num == 2 else 0
    b = 255 if num == 3 else 0
else:
    r = int(input("Red  : "))
    b = int(input("Blue : "))
    g = int(input("Green: "))

for a in range(16):
    strip.setPixelColorRGB(a,r,g,b)
    strip.show()
