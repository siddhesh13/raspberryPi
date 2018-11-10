#We’ll be using the Adafruit DHT11 Python library. You can download the library using Git, so if you don’t have Git installed on your Pi already, enter this at the command prompt:

#sudo apt-get install git-core

#Note: If you get an error installing Git, run sudo apt-get update and try it again.
#To install the Adafruit DHT11 library:

#1. Enter this at the command prompt to download the library:

#git clone https://github.com/adafruit/Adafruit_Python_DHT.git

#2. Change directories with:

#cd Adafruit_Python_DHT

#3. Now enter this:

#sudo apt-get install build-essential python-dev

#4. Then install the library with:

#sudo python setup.py install




import sys
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 23)
    #lcd.write_string("Temp: %d C" % temperature)
    print "Temperature: ",temperature
    print "humidity: ", humidity
