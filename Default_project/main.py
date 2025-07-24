# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
#
#   DESIGNER NAME:  YOUR_NAME
#
#       FILE NAME:  FILE_NAME.py
#
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This file is the source code intended to run on Raspberry Pi 4 or 5.
#   It ....
#
#   Hardware/GPIO Connections:
#     - GPIO18 (Pin 12)  - Input connected to the pushbutton.
#
# *****************************************************************************

#---------------------------------------------------
# Python Modules used in program
#---------------------------------------------------
import gpiod as GPIO

#---------------------------------------------------
# Constants to be used in program
#---------------------------------------------------
# GPIO number based on BCM numbering scheme
BUTTON_PIN = 18
CHIP_NAME  = "gpiochip4"   # Pi 5 uses gpiochip4; use "gpiochip0" for Pi 4



# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function sets up the GPIO pin using libgpiod. It configures one GPIO
#   line as input with an internal pull-up resistor.
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   chip        - gpiod.Chip object
#   button_line - gpiod.Line object for LED output
# -----------------------------------------------------------------------------
def setup_gpio():
  # Open the GPIO chip

  # Get the requested line for the button


  return (gpio_chip, button_line)



#---------------------------------------------------------------------
#  main() function
#---------------------------------------------------------------------
def main():
  #-------------------------------------
  # Variables local to this function
  #-------------------------------------



# Call the main function when the script is run directly
if __name__ == '__main__':
  main()
