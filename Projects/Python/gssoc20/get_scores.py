import requests
from selenium import webdriver
import time
import playsound

f = open('gssoc_peeps.txt', 'r').readlines()

driver = webdriver.Firefox(executable_path='./geckodriver')

URL = "https://www.gssoc.tech/profile.html"

score_file = open('score.txt', 'a')

for i in range(len(f)):
    run = True
    driver.get(URL)
    a = driver.find_elements_by_xpath('//*[@id="usernameSearchInput"]')
    name = f[i]
    a[0].send_keys(name)
    time.sleep(1)
    driver.find_elements_by_xpath('//*[@id="usernameSearchButton"]')[0].click()
    score_element = None
    while run:
        try:
            score_element = driver.find_element_by_css_selector('#userScoreOutput')
        except:
            pass
        if score_element != None:
            score = score_element.text
            run = False

    if int(score) > 58:
        playsound.playsound('attack.wav')
    else:
        playsound.playsound('applause7.wav')
    
    print(name + " : " + score)
    try:
        score_file.write(str(score) + " ")
        score_file.write(name)
    except:
        print("ERROR FETCHING THIS ONE. TRYING NEXT ONE")
    time.sleep(65)

score_file.close()