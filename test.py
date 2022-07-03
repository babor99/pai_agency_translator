from lib2to3.pgen2 import driver
import time
from selenium import webdriver
import selenium 
from selenium.webdriver.common.by import By


# Give Language code in which you want to translate the text:=>
lang_code = 'bengali '

# Provide text that you want to translate:=>
input1 = " Coronaviruses are a group of related viruses that cause diseases in mammals and birds. In humans, coronaviruses cause respiratory tract infections that can be mild, such as some cases of the common cold (among other possible causes, predominantly rhinoviruses), and others that can be lethal, such as SARS, MERS, and COVID-19. Symptoms in other species vary: in chickens, they cause an upper respiratory tract disease, while in cows and pigs they cause diarrhea. There are yet to be vaccines or antiviral drugs to prevent or treat human coronavirus infections."

# launch browser with selenium:=>
browser = webdriver.Chrome() #browser = webdriver.Chrome('path of chromedriver.exe file') if the chromedriver.exe is in different folder

# copy google Translator link here:=>
browser.get("https://translate.google.com/?sl=auto&tl="+lang_code+"&text="+input1+"&op=translate")

# just wait for some time for translating input text:=>
time.sleep(5)

# Given below x path contains the translated output that we are storing in output variable:=>
output1 = browser.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]').text
# output1 = browser.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]').text

# Display the output:=>
print("Translated Paragraph:=> " + output1)

with open('some.txt', 'w', encoding='utf-8') as txt:
    txt.write(output1)

browser.close()