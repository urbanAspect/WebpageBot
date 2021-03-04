from selenium import webdriver
import time

aprapa = [165, 173, 111, 117, 129, 134, 141, 141, 189, 197, 238, 42, 63, 107, 147, 186]

PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

pageNumber = int(input('Please input a number: '))
pageNumber -= 1
pageNumber = pageNumber * 24

nextPageName = "https://otroski.rtvslo.si/infodrom/news/archive/1/" + str(pageNumber) + "/"

driver.get(nextPageName)

time.sleep(0)

quit()