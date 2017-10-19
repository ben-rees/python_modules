import time		# Import this to use the sleep(wait) command
import RPi.GPIO as IO	# Import this to use the GPIO pins

IO.setmode(IO.BOARD)	# Setting the pin numbering convention
IO.setup(11,IO.OUT)	# Setting pin 11 as my output(3.3v)

class LedPulse:		# Creating a class containing the LED pulse programming to be later given an object

	def pulse(self):	# Defining the function that needs to run in order to oulse the LED when called later

		p = IO.PWM(11,50)	# PWM = Pulse width modulation. 11 is my channel(pin)
					# and 50 is the frequency in Hz
		p.start(0)		# This starts the pulsing with a DutyCycle of 0 (off)
					# The DutyCycle determines on long the LED in on for
					# during each cycle. 0(0%) is never and 100(100%) is
					# always.

		try:				# This try block gives a safe way to exit this loop
			while True:		# cleanly. Ctrl-C will stop the pwm and run IO.cleanup

				for i in range(50):	# Cycles variable "i" from 0-50. I will
							# later double the value so I only have 
							# to count up to 25

					p.ChangeDutyCycle(i*2)		# Each time i counts up it change the duty
									# cycle so the LED gets brighter. I'm
									# multiplying it by 2 so it cycles from
									# 0-100 quicker

					time.sleep(0.02)		# Gives a slight pause before the cycle
									# reverses

				for i in range(50):			# Setting up another 50 count

					p.ChangeDutyCycle(100-(i*2))	# Using i to subtract from 100
									# resulting in the LED dimming

					time.sleep(0.02)		# Another pause


		except KeyboardInterrupt:	# When I try block fails (broken loop in this
						# case) the Python will move onto the next
						# except block. This is how we can safely exit)

			print("Terminated by user")	# KeyboardInterrupt: is looking for code to
							# follow it. I could use pass to null it
							# but instead I'm giving user feedback.

		p.stop()	# Stops the pulsing set at the beginning

		IO.cleanup()	# Resets the GPIO states back to default ready for
				# new code

		print("Cleanup complete")	# Confirmation the the cleanup ran


#run = LedPulse()

#run.pulse()
