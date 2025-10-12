import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import xmlrunner

class Test(unittest.TestCase):
    def setUp(self):
        options = Options()
        prefs = {
            "profile.default_content_settings.popups": 0,
            "directory_upgrade":True
        }
        options.add_experimental_option("prefs",prefs)
        options.add_argument('start-maximized')
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)


    def test_title(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def test_mercado_libre(self):

        options = Options()
        prefs = {
            "profile.default_content_settings.popups": 0,
            "directory_upgrade":True
        }
        options.add_experimental_option("prefs",prefs)
        options.add_argument('start-maximized')
        #options.add_argument("--headless")

        #self.driver = webdriver.Chrome(service=ChromeService("../Drivers/chromedriver.exe"), options=options)

        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        
        self.driver.get("https://www.mercadolibre.co.cr/")
        self.driver.find_element("xpath","//input[@id='cb1-edit']").send_keys("Play Station 5")
        self.driver.find_element("xpath","//input[@id='cb1-edit']").send_keys(Keys.ENTER)
        self.assertIn("Playstation 5 Pro 2tb Avenida Tecnologica", self.driver.find_element("xpath","//a[normalize-space()='Playstation 5 Pro 2tb Avenida Tecnologica']").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'))
