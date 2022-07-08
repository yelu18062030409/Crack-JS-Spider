from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get('https://www.yangkeduo.com/')
js = open(r'F:\Crack-JS-Spider\拼多多\anti_content.js', mode='r', encoding='utf-8').read()
print(js)
print(driver.execute_script(js))
print('-----------------------')
for i in range(10):
    anti=driver.execute_script("return result.messagePack()")
    print(anti)
    print(len(anti))
input('回车关闭')
driver.quit()
