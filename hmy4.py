#!/usr/bin/env python
import sys
#print(sys.path)
from splinter import Browser
import time
import datetime
import os
from pyvirtualdisplay import Display
from datetime import datetime

non_display = True


display = None
if non_display:
    display = Display(visible=0, size=(1024, 768))
    display.start()


url = "http://jiaju.sina.com.cn/zt/jjhyzpb/"
url = "http://survey.news.sina.com.cn/survey.php?id=111468"
count = 1
while True:
    with Browser() as browser:
        tt = time.strftime('%Y-%m-%d %X', time.localtime())
        print(tt)
        print("visit %s, %d" % (url,count))
        browser.cookies.delete()
        box = None
        try:
            browser.visit(url)
            print("sleeping..")
            time.sleep(1)
            for _box in browser.find_by_name("q_129489[]"):
                if _box.value=='558108':
                    box = _box
                    break
            if box!=None:
                print(box.value)
                box.click()
                time.sleep(2)
                #button = browser.find_by_xpath("//*[contains(@class, 'sv_buttons')]/input")
                button = browser.find_by_id("JS_Survey_Submit")
                #print(len(button))
                #button = button[0]
                button.click()
                time.sleep(4)
                print(browser.title.encode("utf-8"))
                #browser.cookies.delete()
            else:
                print("non box")
        except Exception, e:
            print e
    aa = os.system('nmcli con down uuid 00962828-73a9-4073-8f2f-6045c0d262f1')
    time.sleep(2)
    aa = os.system('nmcli con up uuid 00962828-73a9-4073-8f2f-6045c0d262f1')
    time.sleep(1)

if non_display:
    display.stop()
