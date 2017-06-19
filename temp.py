import sys
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 23)
    #lcd.write_string("Temp: %d C" % temperature)
    print "Temperature: ",temperature
    print "humidity: ", humidity
    
