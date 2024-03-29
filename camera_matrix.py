# NOTE:  I needed to change permissions on /dev/vchiq to make this work...
# Also needed to chmod 666 temp.jpg

# For the camera...
from picamera import PiCamera

# used to slow down our main loop
from time import sleep 

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw


# this is the size of ONE of our matrixes. 
matrix_rows = 32
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 1 
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

###################################
# Main loop 
###################################
camera = PiCamera()
camera.capture('temp.jpg')
image = Image.open("temp.jpg").convert('RGB')
image = image.resize((32,32))
matrix.SetImage(image, 0, 0)

try:
  print("Press CTRL-C to stop")
  while True:
    camera.capture('temp.jpg')
    image = Image.open("temp.jpg").convert('RGB')
    image = image.resize((32,32))
    matrix.SetImage(image, 0, 0)
    sleep(2)

except KeyboardInterrupt:
  exit(0)
