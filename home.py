import time
import datetime
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from soundmanager.sound import *

import win32gui
import win32con

def open_icloud(link, profile_number, positions, sizes, email, password) : 
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\'User Data'\\Profile%s"%str(profile_number)) #Path to your chrome profile
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

    driver.get(link)

    delay = 20
    try : 
        WebDriverWait(driver, delay).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'auth-frame')))
    except : 
        driver.switch_to.frame('auth-frame')
        pass
    time.sleep(5)
    email_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'account_name_text_field')))
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    password_input = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, 'password_text_field')))
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    driver.set_window_position(positions[0], positions[1])
    driver.set_window_size(sizes[0], sizes[1])
    return driver

def play_youtube(link, minutes, volume) : 
    Sound.volume_set(volume)

    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\'User Data'\\Profile3") #Path to your chrome profile

    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
    driver.get(link)

    try : 
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']"))).click()
    except :
        pass

    now = datetime.datetime.today()
    future = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute+minutes)
    print(now, future)
    time.sleep((future-now).seconds)
    driver.quit()
    return

def play_bbc(link, minutes, volume) :
    # volume should be adjusted
    Sound.volume_set(volume)

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(link)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'jwppp-video-box-801'))).click()

    now = datetime.datetime.today()
    future = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute+minutes)
    print(now, future)
    time.sleep((future-now).seconds)
    driver.quit()
    return

def monitor_turn_on() : 
    #turn on use :-
    win32gui.SendMessage(win32con.HWND_BROADCAST,
                 win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)
    return

def monitor_turn_off() :
    #to turn off use :-
    win32gui.SendMessage(win32con.HWND_BROADCAST,
                     win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
    return


