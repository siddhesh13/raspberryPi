"""
Interfacing Raspberry Pi and MPU-6050


Once you have the board connected you can test to see if the Pi has detected it.  This is done with the following command to install the i2c tools
sudo apt-get install i2c-tools
and then either
sudo i2cdetect -y 0 (for a Revision 1 board like mine)
or
sudo i2cdetect -y 1 (for a Revision 2 board)
then you should see output showing any I2C devices that are attached and their addresses

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --

This shows that the Pi has detected the sensor with an address of 0x68 (hexadecimal), this address is needed to interact with it.  Enter the following command and you should get an output of 0x68 on screen if everything is working properly.
sudo i2cget -y 0 0x68 0x75
This command talks to the device whose address is 0x68 (the sensor) and retrieves the value in the register 0x75 which has a default value of 0x68 the same value as the address.

To be able to read from the I2C using Python bus we need to install the smbus module
sudo apt-get install python-smbus 

Now to some code, this is just simple test code to make sure the sensor is working 

"""

import smbus

import math

# Power management registers

power_mgmt_1 = 0x6b

power_mgmt_2 = 0x6c

def read_byte(adr):

    return bus.read_byte_data(address, adr)

def read_word(adr):

    high = bus.read_byte_data(address, adr)

    low = bus.read_byte_data(address, adr+1)

    val = (high << 8) + low

    return val

def read_word_2c(adr):

    val = read_word(adr)

    if (val >= 0x8000):

        return -((65535 - val) + 1)

    else:

        return val

def dist(a,b):

    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):

    radians = math.atan2(x, dist(y,z))

    return -math.degrees(radians)

def get_x_rotation(x,y,z):

    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards

address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode

bus.write_byte_data(address, power_mgmt_1, 0)

print "gyro data"

print "---------"

gyro_xout = read_word_2c(0x43)

gyro_yout = read_word_2c(0x45)

gyro_zout = read_word_2c(0x47)

print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)

print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)

print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)

 

print

print "accelerometer data"

print "------------------"

accel_xout = read_word_2c(0x3b)

accel_yout = read_word_2c(0x3d)

accel_zout = read_word_2c(0x3f)

 

accel_xout_scaled = accel_xout / 16384.0

accel_yout_scaled = accel_yout / 16384.0

accel_zout_scaled = accel_zout / 16384.0

print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled

print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled

print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled
print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
