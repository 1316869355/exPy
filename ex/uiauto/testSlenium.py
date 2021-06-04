# -*- coding:utf-8 -*-
from selenium import webdriver

browser=webdriver.Chrome()
# browser.get("http://www.baidu.com")
browser.get("http://inventwithpython.com")

'''
    查找元素
    find_element_* 返回页面匹配的第一个元素
    find_elements_* 返回页面中匹配的所有元素列表
    未找到元素 会抛出 NoSuchElement异常
    元素 方法
    tag_name
    get_attribute(name)
    text
    clear()
    is_displayed()
    is_enabled()
    is_selected()
    location   字典，表示该元素在页面上的位置
'''
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except Exception as e:
    print('err msg: ', e)
    print('Was not able to find an element with that name.')

# print(driver.page_source)
