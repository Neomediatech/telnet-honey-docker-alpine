import re
import random
import time
import json
import traceback

import struct
import socket
import select
import errno

from dbg    import dbg

MIN_FILE_SIZE = 128
PROMPT = " # "
			
class Session:
	def __init__(self, output, remote_addr):
		dbg("New Session")
		self.output      = output
		
		self.remote_addr = remote_addr

		# Files already commited
		self.files = []

	def login(self, user, password):
		dbg("Session login: user=" + user + " password=" + password)
		
		self.send_string(PROMPT)

	def end(self):
		dbg("Session End")

	def send_string(self, text):
		self.output(text)


