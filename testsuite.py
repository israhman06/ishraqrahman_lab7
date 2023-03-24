import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
SPI_PORT=0
SPI_DEVICE = 0

mcp = Adafruit_MCP3008.MCP3008(spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE))

ledPin = 11
GPIO.setup(11, GPIO.OUT)
lightThreshold = 300
soundThreshold = 550
   
if __name__ == '__main__':
	while (True):
		#Test 1
		num1=5
		for _ in range(num1):

			GPIO.output(ledPin, 1)
			time.sleep(.5)
			GPIO.output(ledPin, 0)
			time.sleep(.5)

		#Test 2
		start = time.time()
		while (time.time() - start)<5:
			lightValue = mcp.read_adc(0)
			# print(lightValue)
			if lightValue > lightThreshold:
				print("bright")
			else:
				print("dark")
			time.sleep(0.1)

		#Test 3
		num2 = 4
		for _ in range(num2):
			GPIO.output(ledPin, 1)
			time.sleep(.2)
			GPIO.output(ledPin, 0)
			time.sleep(.2)

		# Test 4
		start1 = time.time()
		while (time.time() - start1)<5:
			soundValue = mcp.read_adc(1)
			print(soundValue)
			if (soundValue > soundThreshold):
				GPIO.output(ledPin, 1)
				time.sleep(.1)
				GPIO.output(ledPin, 0)
				time.sleep(.1)
			time.sleep(0.1)
