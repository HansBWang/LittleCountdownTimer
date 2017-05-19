import os
import time
import sys, getopt

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

def countdown(n):
	for i in range(0,n):
		seconds = n-i
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		print("{:02d}:{:02d}:{:02d}".format(h, m, s))
		time.sleep(1)
	# Calling the notification function
	notify(title    = "Time's up!",
	       subtitle = 'Take a break~',
	       message  = "Hello, it's time to take a break!")

def main(argv):
	sec = 0
	try:
		opts, args = getopt.getopt(argv,"hs:",["help","seconds="])
	except getopt.GetoptError as err:
		print err
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h","--help"):
			print 'countdownTimer.py -s <sec>'
			sys.exit()
		elif opt in ("-s", "--seconds"):
			sec = int(arg)

	if sec>0:
		countdown(sec)


if __name__ == "__main__":
   main(sys.argv[1:])