from selenium import webdriver
from selenium.webdriver.common import desired_capabilities as DC
from Modules import reserve, sendEmail
import winsound, time


# 预约档案信息
recordNumber = '201708020063955'
questionText = '您父亲的年龄？'
questionAnswer = '40'
months_after_current_month = 0  # 在当前月份后的第几个月，例如：当前月份是八月，该参数为1则查看九月的预约情况
startDate = '2017-08-01' # 可选参数，设定所需查看的起始日期
endDate = '2017-08-31' # 可选参数，设定所需查看的结束日期
max_trails = 5
time_to_pause = 3

# 模拟浏览器操作
browser = reserve.initiate_browser()
browser = reserve.enter_reservation_page(browser,recordNumber,questionText,questionAnswer)

# 持续刷新页面，直到发现可预约时间，之后通过蜂鸣声和邮件报警
if isinstance(browser, str): # 如果browser为字符串，则为报警信息，直接输出
    print(browser)
else:
    while True:
        browser = reserve.load_reservation_page(browser, months_after_current_month, max_trails)
        result = reserve.findAvailableAppo(browser, startDate, endDate)
        if result:
            for i in range(20):
                winsound.PlaySound('beepSound.wav', winsound.SND_FILENAME)
            #sendEmail.sendNotificationEmail()
            print('邮件发送成功')
            break
        time.sleep(time_to_pause)
        browser = reserve.reload(browser)