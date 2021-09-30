# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # driver  = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')

# # driver.get("https://google.com")
# # #https://nmtt.gov.in/programs/cesme/PMMMNMTT-2019-100001?type=archived

# # print(driver.title)
# # time.sleep(2)
# # search_bar = driver.find_element_by_name("q")

# # search_bar.clear()
# # search_bar.send_keys("metallica")
# # search_bar.send_keys(Keys.RETURN)

# # print(driver.current_url)

# # driver.close()

# driver  = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')

# driver.get("https://chercher.tech/practice/table")
# #https://nmtt.gov.in/programs/cesme/PMMMNMTT-2019-100001?type=archived
# driver.maximize_window()

# print(driver.title)
# time.sleep(2)

# # ele1 = driver.find_element_by_xpath("//table[@id='webtable']/tbody/tr/th[2]").text

# text = driver.find_elements_by_xpath("*/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/th")
# print(text)
# # search_bar = driver.find_element_by_name("q")

# # search_bar.clear()
# # search_bar.send_keys("metallica")
# # search_bar.send_keys(Keys.RETURN)

# # print(driver.current_url)

# driver.close()

code = {"hello":1,"hi":2}
codes = ["hello","hi"]
with open("./test/legend.txt","w") as file:
    for i in codes:
        line = i+":"+str(code[i])+"\n"
        file.write(line)

file.close()