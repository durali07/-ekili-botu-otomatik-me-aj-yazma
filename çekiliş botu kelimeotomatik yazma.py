import click
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
import random
from random import choice
import os
import requests
from bs4 import BeautifulSoup
import locale
import pyautogui
import pywhatkit
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import smtplib
from email.message import EmailMessage

print("twitch adı")
isim = input()
isim = isim.lower()
twitch = "https://www.twitch.tv/"
print("ne yazılacak")
kelime = input()
print("kaç saniyede bir yazabiliyoruz")
saniye = int(input())
print("kendi kulanıcı hesabın")
eposta = input()
print("password")
passwordd = input()

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.twitch.tv/'+isim)
time.sleep(2)
login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button')
login.click()
time.sleep(2)
email = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[1]/div/div[2]/input')
password = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div/div[1]/div[2]/div[1]/input')
giriş = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div')
email.send_keys(eposta)
password.send_keys(passwordd)
giriş.click()
print("20 saniye bekiyoruz")
time.sleep(30)
driver.get(twitch+isim)

while True:
    time.sleep(saniye)
    driver.implicitly_wait(3)
    alll = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[1]/div[2]/div/div/div[1]/div/textarea')
    alll.click()
    driver.implicitly_wait(3)
    onay = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div/div[3]/button')
    onay.click()
    ts = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[1]/div[2]/div/div/div[1]/div/textarea')
    ts.click()
    driver.implicitly_wait(3)
    ts.send_keys(kelime)
    gönder = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[2]/div[3]/div/button/div")
    gönder.click()
    

    
    
#/html/body/div[5]/div/div/div/div/div/div/div[3]/button