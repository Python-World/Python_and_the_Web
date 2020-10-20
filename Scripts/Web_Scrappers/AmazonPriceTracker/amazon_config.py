from selenium import webdriver

DIRECTORY = 'reports'
NAME = input('Enter the search term: ')
CURRENCY = '₹'
MIN_PRICE = int(input('\nEnter the minimum price for filtered search: '))
MAX_PRICE = int(input('\nEnter the maximum price for filtered search: '))
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.in/"


def get_chrome_web_driver(options):
    return webdriver.Chrome("G:/AmazonPriceTracker/chromedriver.exe", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')
