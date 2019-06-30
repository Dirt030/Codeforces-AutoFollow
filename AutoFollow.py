#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver

browser = webdriver.Chrome()


# In[2]:


#Login your account

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser.get("http://codeforces.com/enter")
try:
    hoe = browser.find_element_by_id("handleOrEmail")
    hoe.send_keys("****") #<------Here is your username
    pas = browser.find_element_by_id("password")
    pas.send_keys("************") #<------Here is your password
    pas.send_keys(Keys.ENTER)
    #if you can not automatically login, maybe there is something wrong here. Because I choose Enter instead of Click.
except NoSuchElementException:
    pass
except:
    print("Unknown error occured, pls email me on 280538483@qq.com.\n")
    browser.close()


# In[3]:


#Load friends' info

import pandas as pd

try:
    friends = pd.read_csv("Friends.csv")
except FileNotFoundError:
    print("Friends.csv lost or misnamed.\n")
except:
    print("Unknown error occured, pls email me on 280538483@qq.com.\n")


# In[4]:


#Add Friends

from selenium.webdriver.common.action_chains import ActionChains

for i in range(friends.shape[0]):
    try:
        username = friends.loc[i, "Username"]
        browser.get("http://codeforces.com/profile/%s" %username)
        ActionChains(browser).click(browser.find_element_by_css_selector("img[title='Click to add to friends']")).perform()
    except NoSuchElementException:
        pass
    except KeyError:
        print("Friend.csv is damaged.\n")
        browser.close()
    except:
        print("Unknown error occured, pls email me on 280538483@qq.com.\n")
        browser.close()


# In[5]:


print("Mission Complete!")
browser.close()

