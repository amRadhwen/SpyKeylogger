from keylogger import Keylogger
from screenshot import Screenshot

if __name__ == "__main__":
	#mouse_logger = Keylogger("mouse_log.txt")
	#mouse_logger.start_mouse_listener()
	#keyboard_logger = Keylogger("mouse_log.txt","keyboard_log.txt")
	#keyboard_logger.start_listener()
	screenshot = Screenshot("Screenshots", 5)
	screenshot.start_screenshoting()