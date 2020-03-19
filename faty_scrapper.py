from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class DataBot:
	def __init__(self,data):
		self.data = data
		self.bot = webdriver.Firefox()


	def scraper(self):
		bot = self.bot
		bot.get("http://www.puertos.es/es-es/oceanografia/Paginas/portus.aspx/")
		field = bot.find_element_by_class_name("dx-texteditor-input")
		field.clear()

		field.send_keys(self.data)

if __name__ == '__main__':
	ed = DataBot("valencia")
	ed.scraper()