from selenium import webdriver
import time
import random


browser = webdriver.Chrome()
url=("https://eksisozluk.com/mustafa-kemal-ataturk--34712?p=")
pageCount =1
entries=[]
entryCount=1
while pageCount <= 10:
    randomPage = random.randint(1,1971)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    pageCount += 1

    elements= browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    
with open("Desktop\entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n"+entry + "\n")
        file.write("******************\n")
        entryCount+=1

browser.close()        

        
"""for entry in entries:
    print(str(entrtyCount)+"************")
    print(element.text)
    entrtyCount += 1"""



#urlye gidecek
"""elements= driver.find_elements_by_css_selector(".content")

for element in elements:
    print("************")
    print(element.text)"""

