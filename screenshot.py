import pyscreenshot as ImageGrab
from os import path, makedirs
from dateTime import Datetime
import threading
from time import sleep
from RepeatedTimer import RepeatedTimer

class Screenshot:

	def __init__(self, path_name, time):
		self.path_name = path_name
		self.time = time
		self.init_path()

	def take_screenshot(self):
		screenshot = ImageGrab.grab()
		screenshot_name = Datetime().get_date_time()
		self.save_screenshot(screenshot, screenshot_name)

	def start_screenshoting(self):
		screenshotinng_thread = RepeatedTimer(self.time, self.take_screenshot)
		try:
			sleep(self.time+5)
		finally:
			screenshotinng_thread.stop()

	def init_path(self):
		if not path.exists(self.path_name):
			makedirs(self.path_name)
			return True
		return False

	def save_screenshot(self, screenshot, screenshot_name):
		screenshot.save(self.path_name + "/" + screenshot_name + ".png")
		return True
