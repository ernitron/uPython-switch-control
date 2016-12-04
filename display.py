# Micropython Http Temperature Server
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

display = None

def display_temp(text1, text2=''):
    global display

    if display == None:
      try:
        import ssd1306
        from machine import I2C, Pin
        i2c = I2C(sda=Pin(4), scl=Pin(5))
        display = ssd1306.SSD1306_I2C(64, 48, i2c, 60)
        print ("opening display again")
      except:
        display == False
        return
    else:
        display.fill(1)
        display.show()
        display.fill(0)
        display.text(text1,0, 10, 1)
        display.text(text2,0, 20, 1)
        display.show()
