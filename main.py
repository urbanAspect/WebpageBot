from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('all packages imported')

searchwords = [
    'google', 'programer', 'vdrl', 'nagrado', 'nagrada', 'hack'
]
pages = []

pageNum = 1
pageIndex = 0

PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://otroski.rtvslo.si/infodrom/news/archive/1/0/")
print(driver.title)

for k in range(247):
    # next page link
    pageIndex = str(pageIndex)
    nextPageName = "https://otroski.rtvslo.si/infodrom/news/archive/1/" + pageIndex + "/"

    # get the text from the page
    try:
        searchText = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "TopSection"))
        )
    except:
        driver.quit()

    # put the text in a file
    file = searchText.text

    # search for a word from list in file
    for i in range(5):
        if searchwords[i] in file:
            pages.append(pageNum)
        else:
            pass
    pageNum = pageNum + 1

    # move to the next page
    try:
        driver.get(nextPageName)
        print('next page opened succesfuly ' + str(pageNum - 1))
    except:
        quit()
    pageIndex = int(pageIndex)
    pageIndex += 24


print(pages)

driver.quit()

[412, 667, 852, 858, 870, 875, 882, 883, 931, 938, 979, 1030, 1051, 1095, 1135, 1174]