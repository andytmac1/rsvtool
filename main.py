import module1
import winsound, time

# 预约档案信息
recordNumber = '201707250191841'
questionText = '您父亲的姓名？'
questionAnswer = '朱晓中'

# 模拟浏览器操作
browser = module1.webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
browser.get('http://ppt.mfa.gov.cn/appo/index.html')
browser.set_page_load_timeout(5)
browser = findDoc(browser,recordNumber,questionText,questionAnswer)

# 持续刷新页面，直到发现可预约时间，之后通过蜂鸣声和邮件报警
while 1:
    browser = loadingPage(browser, 5, 1)
    if isAvailableAppoExisted(browser):
        for i in range(20):
            winsound.PlaySound('beepSound.wav',winsound.SND_FILENAME)
        sendNotificationEmail()
        print('发送成功')
        break
    time.sleep(3)
    try:
        browser.refresh()
    except TimeoutException:
        browser.close()
        browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
        browser.get('http://ppt.mfa.gov.cn/appo/index.html')
        browser.set_page_load_timeout(5)
        browser = findDoc(browser, recordNumber, questionText, questionAnswer)
        break



