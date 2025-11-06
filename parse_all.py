from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions, ChromeService
from selenium.webdriver.common.by import By
from Car import Car
import parsers.drom_parser as drom_parser, parsers.avito_parser as avito_parser, parsers.sberauto_parser as sberauto_parser
from mysql import MySQL


options = ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--disable-notifications')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument(f'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0')

service = ChromeService()

driver = webdriver.Chrome(options = options, service=service)

mysql = MySQL()

cars1 = drom_parser.parse(driver)
mysql.add(cars1)
cars2 = avito_parser.parse(driver)
mysql.add(cars2)
cars3 = sberauto_parser.parse(driver)
mysql.add(cars3)

mysql.delete_duplicates()



