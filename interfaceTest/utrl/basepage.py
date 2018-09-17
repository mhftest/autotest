import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utrl.config import Config
url = Config().get ('URL')

class BasePage (object):
    def get_url(self):
        return url

