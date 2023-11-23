import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# delay plus create the HID

time.sleep(1)
kbd = Keyboard(usb_hid.devices)

# setting up the pins

rows = []
row_pins = [board.GP14, board.GP13, board.GP12, board.GP11]
for row in row_pins:
    row_key = digitalio.DigitalInOut(row)
    row_key.direction = digitalio.Direction.OUTPUT
    rows.append(row_key)

columns = []
column_pins = [
                board.GP0,
                board.GP1,
                board.GP2,
                board.GP3,
                board.GP4,
                board.GP5,
                board.GP6,
                board.GP7,
                board.GP8,
                board.GP9,
                board.GP10
]
for column in column_pins:
    column_key = digitalio.DigitalInOut(column)
    column_key.direction = digitalio.Direction.INPUT
    column_key.pull = digitalio.Pull.DOWN
    columns.append(column_key)

keymap = [
    Keycode.Q,
    Keycode.W,
    Keycode.E,
    Keycode.R,
    Keycode.T,
    Keycode.Y,
    Keycode.U,
    Keycode.I,
    Keycode.O,
    Keycode.P,
    Keycode.BACKSPACE,
    Keycode.A,
    Keycode.S,
    Keycode.D,
    Keycode.F,
    Keycode.G,
    Keycode.H,
    Keycode.J,
    Keycode.K,
    Keycode.L,
    Keycode.SEMICOLON,
    Keycode.ENTER,
    Keycode.Z,
    Keycode.X,
    Keycode.C,
    Keycode.V,
    Keycode.B,
    Keycode.N,
    Keycode.M,
    Keycode.COMMA,
    Keycode.PERIOD,
    Keycode.UP_ARROW,
    Keycode.RIGHT_CONTROL,
    Keycode.LEFT_ALT,
    Keycode.LEFT_SHIFT,
    Keycode.GUI,
    Keycode.ONE,
    None,
    Keycode.SPACEBAR,
    None,
    Keycode.TWO,
    Keycode.LEFT_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.RIGHT_ARROW,
]


while True:
    for r in rows: 
        r.value=1 
        for c in columns: 
            if c.value: 
                while c.value: 
                    time.sleep(0.01) 
                key = rows.index(r) * 11 + columns.index(c) 
                kbd.press((keymap[key])) 
                kbd.release_all() 
        r.value=0