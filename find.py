import csv 
import time
import random
from datetime import datetime
from selenium.webdriver.common.by import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from urllib.parse import parse_qs


options = webdriver.ChromeOptions() 
driver = webdriver.Chrome('./chromedriver', chrome_options=options)  # Optional argument, if not specified will search path.
driver.get('https://www.google.com/search?q=google')












def find_ln(email,force=False):
    url=email+" site:linkedin.com"
    driver.execute_script("window.location='https://www.google.com/search?q="+url+"'")

    f = open("./status", "r")
    if f.read() == '0':
        tm=int(input("Please enter Time:"))   
        
        f = open("status", "w")
        f.write("1")
        f.close()

    if driver.find_elements(By.ID, "captcha-form"):
        tm=input("Please enter Time:") 
        f = open("status", "w")
        f.write("1")
        f.close()

    lnks=driver.find_elements(By.TAG_NAME, "a")
    for lnk in lnks:
        url=lnk.get_attribute('href')
        if(url):
            if url.find('linkedin.com/in/') > -1:
                return url

    



    f = open("./status", "r")
    if f.read() == '0':
        tm=int(input("Please enter Time:"))   
        
        f = open("status", "w")
        f.write("1")
        f.close()
    return False


# time.sleep(random.randint(6, 9))
# print(find_ln('mike@mtg-solution.com'))


r=[]
file = open('data.csv')
csvreader = csv.reader(file)
c=0
founded=0
unfounded=0
for row in csvreader:
    
    f = open("./status", "r")
    if f.read() == '0':
        tm=int(input("Please enter Time:"))   
        
        f = open("status", "w")
        f.write("1")
        f.close()

    ln=find_ln(row[2])
    r=row
    if ln:
        founded=founded+1
    else:
        unfounded=unfounded+1
    r.append(ln)
    f = open('export.csv', 'a')
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(r)


    print('Scanned='+str(c)+' Founded='+str(founded)+' Not Founded='+str(unfounded)+' time='+datetime.now().strftime("%H:%M:%S"))
    time.sleep(random.randint(6, 9))
    c=c+1   
driver.quit()