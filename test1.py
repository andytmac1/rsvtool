from selenium import webdriver
from selenium.webdriver.common import desired_capabilities as DC
from Modules import reserve, sendEmail
import winsound, time


# 预约档案信息
recordNumber = '201708010291318'
questionText = '您父亲的姓名？'
questionAnswer = '张全'
months_after_default_month = 1
max_trails = 5
time_to_pause = 3

# 模拟浏览器操作
browser = reserve.initiate_browser()
browser = reserve.enter_reservation_page(browser,recordNumber,questionText,questionAnswer)
browser = reserve.load_reservation_page(browser, months_after_default_month, max_trails)
fc_events = browser.find_elements_by_class_name('fc-event')
print(len(fc_events))
for i in range(len(fc_events)):
    print(i, fc_events[i-1].text, fc_events[i-1].get_attribute("style"))