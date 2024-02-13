import arrow

class Datetime:
	def __init(self):
		pass
	def get_date_time(self):
		date_time = arrow.now().format("YYYY-MM-DD HH:mm:ss")
		return "["+date_time+"] "