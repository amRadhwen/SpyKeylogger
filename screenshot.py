import pyscreenshot as ImageGrab
from os import path, makedirs
from dateTime import Datetime
from time import time, sleep

class Screenshot:

	def __init__(self, path_name, time, screenshot_log_filename):
		self.path_name = path_name
		self.time = time
		self.screenshot_log_filename = screenshot_log_filename
		self.init_path()

	def take_screenshot(self):
		screenshot = ImageGrab.grab()
		screenshot_name = Datetime().get_date_time()
		self.save_screenshot(screenshot, screenshot_name)
		self.write_screenshot_log(self.screenshot_log_filename, screenshot_name)

	def start_screenshoting(self):
		starttime = time()
		while(True):
			print("Screenshot !")
			self.take_screenshot()
			sleep(self.time - ((time() - starttime) % self.time))

	def init_path(self):
		if not path.exists(self.path_name):
			makedirs(self.path_name)
			return True
		return False

	def save_screenshot(self, screenshot, screenshot_name):
		screenshot.save(self.path_name + "/" + screenshot_name + ".png")
		return True

	def write_screenshot_log(self, screenshot_log_filename, input):
		with open(screenshot_log_filename, "a+") as screenshot_log:
			screenshot_log.write(input+"\n")
		return True
