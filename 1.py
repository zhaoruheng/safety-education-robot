from  selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xlwt
import time
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"')
prefs = {"profile.managed_default_content_settings.images": 2}
#options.add_experimental_option("prefs", prefs)#不加载图片
browser=webdriver.Chrome(chrome_options=options)
WAIT = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)
#####################
def main():

    try:
        browser.get("http://10.16.164.135")
        time.sleep(30)
        print("start")
        cnt=0
        try:
            while 1:
                browser.get("http://10.16.164.135/redir.php?catalog_id=121&object_id=2737")
                time.sleep(245)
                cnt=cnt+4
                print("已刷时间:%d mins"%(cnt))
        finally:
            print("Refresh Failed")
    finally:
        0

main()
