
#coding:utf-8

from selenium import webdriver
class Spider:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://cq.58.com/chuzu/?PGTID=0d100000-0002-5a98-d53b-70a83c225996&ClickID=1')

    def print_content(self):
        contents=self.driver.find_elements_by_class_name("des")
        i=1
        for cont in contents:
            print(str(i)+"."+cont.text+"\n")
            i+=1
        self.driver.quit()

Spider().print_content()