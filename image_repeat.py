# NOTE:  I needed to change permissions on /dev/vchiq to make this work...
# Also needed to chmod 666 temp.jpg

# used to slow down our main loop
import time 

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 32
matrix_columns = 32 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 5
matrix_vertical = 3

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

###################################
# Main loop 
###################################

try:
  print("Press CTRL-C to stop")
  while True:
    try:
      image = Image.open("temp.jpg").convert('RGB')
    except:
      print "collision!"
      continue

    image = image.resize((total_columns,total_rows))
    matrix.SetImage(image, 0, 0)
    time.sleep(.25)

except KeyboardInterrupt:
  exit(0)
