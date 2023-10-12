from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://mylesthomas.io/")
print(driver.title) # print the title of the website
driver.close()  # closes the current tab (if you have 1 tab, which we do, it closes the browser)
# driver.quit()   # closes the browser