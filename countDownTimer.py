import os
import time

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

if __name__ == "__main__":
	
	n = 10
	for i in xrange(0,n):
		seconds = n-i
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		print "%02d:%02d:%02d" % (h, m, s)
		time.sleep(1)

	# Calling the function
	notify(title    = "Time's up!",
	       subtitle = 'Take a break~',
	       message  = "Hello, it's time to take a break!")