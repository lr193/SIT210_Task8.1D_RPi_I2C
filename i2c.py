import smbus
import time

bus = smbus.SMBus(1)

bus.write_byte_data(0x53, 0x2C, 0x0A)

bus.write_byte_data(0x53, 0x2D, 0x08)

bus.write_byte_data(0x53, 0x31, 0x08)

#time.sleep(0.5)

while True:

    xdata0 = bus.read_byte_data(0x53, 0x32)
    xdata1 = bus.read_byte_data(0x53, 0x33)

    xAccel = ((xdata1 & 0x03) * 256) + xdata0

    if xAccel > 511:
        xAccel -= 1024



    ydata0 = bus.read_byte_data(0x53, 0x34)
    ydata1 = bus.read_byte_data(0x53, 0x35)

    yAccel = ((ydata1 & 0x03) * 256) + ydata0

    if yAccel > 511:
        yAccel -= 1024



    zdata0 = bus.read_byte_data(0x53, 0x34)
    zdata1 = bus.read_byte_data(0x53, 0x35)

    zAccel = ((zdata1 & 0x03) * 256) + zdata0

    if zAccel > 511:
            zAccel -= 1024

    print "Acc X: %d" %xAccel
    print "Acc y: %d" %yAccel
    print "Acc z: %d" %zAccel
    print "\n"

    time.sleep(2)
