import datetime
import traceback
import sys
import os.path
import logging

logging.getLogger('').setLevel(logging.DEBUG)
logging.basicConfig(filename='/data/telnet.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

DEBUG = True

def dbg(msg):
	if DEBUG:
		now  = datetime.datetime.now()
		now  = now.strftime('%Y-%m-%d %H:%M:%S')
		line = traceback.extract_stack()[-2]
		line = os.path.basename(line[0]) + ":" + str(line[1])
		print(now + "   " + line.ljust(16, " ") + "  " + msg)
		sys.stdout.flush()
                logging.info(msg)
