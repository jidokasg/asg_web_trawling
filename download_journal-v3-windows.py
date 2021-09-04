#!/usr/bin/env python
# coding: utf-8

# In[2]:


##Load dependencies and login to site

import pandas as pd
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re

#Get desktop path to set as download path
#=============================================================
def getdesktoppath ():
    return os.path.join (os.path.expanduser ("~"), "desktop")


#Website loading function
#==============================================================
def get_url_and_wait_for_page_load(_driver, url):
    driver.get(url)

desktoppath = getdesktoppath()
desktoppath = desktoppath + r"\" + "asg_dl"

#Set default setting for Chrome Driver when using Selenium 
#=============================================================
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": desktoppath,
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})


#Select your chromedriver
#=============================================================
print("Select your chromedriver")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
chromedriver_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file

driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)



#Select file to get download links
#=============================================================
print('Select the output file to download from')
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file



output_df = pd.read_csv(filename)
download_df = output_df[output_df['download'].notnull()]

get_url_and_wait_for_page_load(driver, 'https://www.sciencedirect.com/journal/forensic-science-international-synergy/issues')
driver.maximize_window()

print("Do you need to login for this journal? y or n")
answer = input()

if answer.lower() == "y":
    
    username = input("Input login ID")
    pw = input("Enter password")
    
    try: 
        driver.find_element_by_id("gh-signin-btn").click()
        driver.find_element_by_id ("bdd-email").send_keys(username)
        driver.find_element_by_id("bdd-elsPrimaryBtn").click()

        driver.find_element_by_id ("bdd-password").send_keys(pw)
        driver.find_element_by_id("rememberMe").click()
        driver.find_element_by_id("bdd-elsPrimaryBtn").click()
    except:
        print('login failed')
        pass
#==============================================================================


# In[6]:


keys = ['article_title','download_url']
output = pd.DataFrame()


import os
import shutil


for index, row in download_df.iterrows():
    article_title = row[3]
    article_url = row[4]
    clean_article_title = re.sub('[^A-Za-z0-9]+', ' ', article_title)
    if article_url[-3:] == 'pdf':
        
        ##if pdf link is available, open the page and download to desktop
        get_url_and_wait_for_page_load(driver,article_url)
        
        time.sleep(7)  
        #get latest downloaded file and rename to title
        
        filename = max([desktoppath + r"\\" + f for f in os.listdir(desktoppath)],key=os.path.getctime)
        print(filename)
        shutil.move(filename,os.path.join(desktoppath, clean_article_title + ".pdf"))

    else:
        #to handle those with [Get Access] or [View PDF] view
        get_url_and_wait_for_page_load(driver,article_url)

        time.sleep(7)     
        
        #check if it's [Get Access] view
        dl_btn = driver.find_elements_by_xpath("//a[contains(@class, 'anchor PdfDrawdownButtonLink u-margin-s-right u-margin-xs-top')]")
        
        #if it's [View PDF] view
        if dl_btn == []:
            print('this is PDF View')
            dl_btn = driver.find_elements_by_xpath("//a[contains(@class, 'link-button link-button-primary')]")
            article_url = dl_btn[0].get_attribute("href")

            time.sleep(7)
            ##if pdf link is available, open the page and download to desktop
            get_url_and_wait_for_page_load(driver,article_url)

            #get latest downloaded file and rename to title
            time.sleep(7)  
            
            filename = max([desktoppath + r"\\" + f for f in os.listdir(desktoppath)],key=os.path.getctime)
            print(filename)
            shutil.move(filename,os.path.join(desktoppath, clean_article_title + ".pdf"))
            
            time.sleep(7)
        
        else:
            print('this is Get Access View')
            #click to go next page
            dl_btn[0].click();

            #driver.switch_to.window(driver.window_handles[1])
            time.sleep(7)        

            #sometimes it will download immediately, sometimes it will require click continue
            #to put a try pass
            #not a good practice but as a workaround
            try:
                driver.switch_to.window(driver.window_handles[1])
                continue_btn = driver.find_elements_by_xpath("//button[@class='button button-primary u-padding-l-hor move-right']")
                
                continue_btn[0].click()
                print('clicked')
                
                time.sleep(7) 
                driver.close()
                time.sleep(4) 
                driver.switch_to.window(driver.window_handles[0])
                
                #get latest downloaded file and rename to title
                filename = max([desktoppath + r"\\" + f for f in os.listdir(desktoppath)],key=os.path.getctime)
                print(filename)
                shutil.move(filename,os.path.join(desktoppath, clean_article_title + ".pdf"))
                
            except:
                print(clean_article_title)
                print('continue button not found')
                pass

    
print('Finish downloading.')
driver.quit()


# In[39]:





# In[41]:





# In[19]:





# In[23]:





# In[ ]:




