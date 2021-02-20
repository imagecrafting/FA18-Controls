import time
import board
import digitalio
# from analogio import AnalogOut
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_circuitplayground.express import cpx

kbd = Keyboard()
apuOn = False
seatArmed = False
ejectionTriggered = False
wingSpread = False
crankRight = False
crankLeft = False
AmbientDark = False
cpx.pixels.brightness = 0.05
cpx.pixels[0] = (155, 0, 0)

# ambientLight = cpx.light
# consoleLighting = AnalogOut(board.A0)

wingFold = digitalio.DigitalInOut(board.A0)
wingFold.direction = digitalio.Direction.INPUT
wingFold.pull = digitalio.Pull.UP
apu = digitalio.DigitalInOut(board.A1)
apu.direction = digitalio.Direction.INPUT
apu.pull = digitalio.Pull.DOWN
eject = digitalio.DigitalInOut(board.A2)
eject.direction = digitalio.Direction.INPUT
eject.pull = digitalio.Pull.UP
engineLeft = digitalio.DigitalInOut(board.A3)
engineLeft.direction = digitalio.Direction.INPUT
engineLeft.pull = digitalio.Pull.UP
engineRight = digitalio.DigitalInOut(board.A4)
engineRight.direction = digitalio.Direction.INPUT
engineRight.pull = digitalio.Pull.UP
seat = digitalio.DigitalInOut(board.A5)
seat.direction = digitalio.Direction.INPUT
seat.pull = digitalio.Pull.UP
repair = digitalio.DigitalInOut(board.A6)
repair.direction = digitalio.Direction.INPUT
repair.pull = digitalio.Pull.UP
vox = digitalio.DigitalInOut(board.A7)
vox.direction = digitalio.Direction.INPUT
vox.pull = digitalio.Pull.UP

while True:
    if wingFold.value:
        if not wingSpread:
            wingSpread = True
            kbd.send(Keycode.SHIFT, Keycode.W)
            kbd.release_all()
            cpx.pixels[0] = (0, 200, 0)
    else:
        if wingSpread:
            wingSpread = False
            kbd.send(Keycode.W)
            kbd.release_all()
            cpx.pixels[0] = (155, 0, 0)
    if apu.value:
        if not apuOn:
            apuOn = True
            kbd.send(Keycode.A)
            kbd.release_all()
            cpx.pixels[5] = (0, 200, 0)
    else:
        if apuOn:
            apuOn = False
            kbd.send(Keycode.SHIFT, Keycode.A)
            kbd.release_all()
            cpx.pixels[5] = (0, 0, 0)
    if seat.value:
        if not seatArmed:
            seatArmed = True
            kbd.send(Keycode.SHIFT, Keycode.T)
            kbd.release_all()
            cpx.pixels[9] = (155, 0, 0)
    else:
        if seatArmed:
            seatArmed = False
            kbd.send(Keycode.T)
            kbd.release_all()
            cpx.pixels[9] = (0, 200, 0)
    if eject.value:
        if not ejectionTriggered:
            ejectionTriggered = True
            kbd.release_all()
            cpx.pixels[8] = (0, 0, 0)
    else:
        if ejectionTriggered:
            ejectionTriggered = False
            kbd.send(Keycode.E)
            kbd.release_all()
            cpx.pixels[8] = (200, 0, 0)
    if repair.value:
        cpx.pixels[4] = (0, 0, 0)
    else:
        kbd.send(Keycode.R)
        kbd.release_all()
        cpx.pixels[4] = (200, 0, 0)
        time.sleep(0.25)
        cpx.pixels[4] = (0, 200, 0)
        time.sleep(0.25)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[7] = (0, 0, 0)
    if vox.value:
        cpx.pixels[6] = (0, 0, 0)
    else:
        kbd.send(Keycode.V)
        kbd.release_all()
        cpx.pixels[6] = (200, 0, 200)
        time.sleep(0.25)
    if cpx.button_b:
        kbd.send(Keycode.F)
        kbd.release_all()
        cpx.pixels[1] = (200, 0, 0)
        time.sleep(0.25)
        cpx.pixels[1] = (0, 200, 0)
        time.sleep(0.25)
    else:
        cpx.pixels[1] = (0, 0, 0)
    if engineRight.value:
        if not crankRight:
            crankRight = True
            kbd.release_all()
    else:
        if crankRight:
            crankRight = False
            kbd.send(Keycode.PERIOD)
            kbd.release_all()
            cpx.pixels[2] = (200, 0, 0)
            time.sleep(0.25)
            cpx.pixels[2] = (0, 200, 0)
            time.sleep(0.25)
    if engineLeft.value:
        if not crankLeft:
            crankLeft = True
            kbd.release_all()
    else:
        if crankLeft:
            crankLeft = False
            kbd.send(Keycode.COMMA)
            kbd.release_all()
            cpx.pixels[7] = (200, 0, 0)
            time.sleep(0.25)
            cpx.pixels[7] = (0, 200, 0)
            time.sleep(0.25)