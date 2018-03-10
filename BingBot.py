#Codded by BOT HAT TBN
#Team Automaton
from csvdb import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import *
print("=======Coded By BOT HAT from TBN======= \n #TeamAutomaton")
def bot():
    users=csv_total_rows("./users.csv")
    i=0
    with open('proxy.txt','r') as f:
        for i, l in enumerate(f):
            pass
        lines=i + 1
    if lines==0:
        loop=1
    elif users<lines:
        loop=users
    else:
        loop=lines
    i=1
    a=1

    
    while i<=loop:
        #root.update()

        try:
            q=str(a)
            username=csv_query('./users.csv','username','slno',q)
            password=csv_query('users.csv','passwords','slno',q)
            try:
                file=open('proxy.txt','r')
                lines=file.readlines()
                PROXY=lines[i]
            except:
                PROXY=''
            file=open('pua.txt','r')
            lines=file.readlines()
            no_of_ua=len(lines)
            rand_pc_ua=randint(1, no_of_ua)
            useragent=lines[rand_pc_ua]
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % PROXY)
            chrome_options.add_argument("--user-agent="+useragent)
            chrome = webdriver.Chrome(chrome_options=chrome_options)
            chrome.get("http://bing.com/")
            time.sleep(15)
            input_element = chrome.find_element_by_id("id_l").click()
            time.sleep(15)
            input_element = chrome.find_element_by_name("loginfmt")
            input_element.send_keys(username)
            input_element = chrome.find_element_by_id("idSIButton9").click()
            time.sleep(10)
            input_element = chrome.find_element_by_name(password)
            input_element.send_keys(password)
            input_element = chrome.find_element_by_id("idSIButton9").click()
            time.sleep(10)
            trying=0
            a=a+1
            while trying<41:
                try:
                    file=open('rando.txt','r')
                    lines=file.readlines()
                    no_of_words =len(lines)
                    rand_word_no=randint(1, no_of_words)
                    word=lines[rand_word_no]
                    time.sleep(10)
                    input_element = chrome.find_element_by_name("q").clear()
                    input_element = chrome.find_element_by_name("q")
                    input_element.send_keys(word)
                except:
                    print("skping search")
                finally:
                    trying=trying+1
        except:
            print("skping proxy "+PROXY)
            i=i+1
        finally:
            chrome.quit()

bot()
