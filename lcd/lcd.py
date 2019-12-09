import lcd_module
from time import *
mylcd = lcd_module.lcd()
mylcd.lcd_display_string("Hello World",1)
mylcd.lcd_display_string("Raspberry Pi3 b+",2)