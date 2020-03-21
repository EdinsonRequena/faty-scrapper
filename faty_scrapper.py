from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class DataBot:
	def __init__(self,data):
		self.data = data
		self.bot = webdriver.Firefox()


	def scraper(self):
		bot = self.bot
		bot.get("https://m.facebook.com/")
		field = bot.find_element_by_class_name("bl")
		field.clear()

		field.send_keys(self.data)

if __name__ == '__main__':
	ed = DataBot("valencia")
	ed.scraper()