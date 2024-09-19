from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv
from os import path



links: list = [
        ["LOQ_R7_8845HS_4050", "https://amzn.in/d/4NL6AvO"],
        ["KatanaA17_R7_8845HS_4060", "https://amzn.in/d/c4Scwyz"]
        ]

data: list  = []
lastUpdatedDate = None

with open('data.csv', 'r') as dataFile:
    read = csv.reader(dataFile)
    for row in read:
        data.append(row)
    lastUpdatedDate = data[-1][-1]


def checkPrice():
    # if data["LOQ_R7_8845HS_4050"][0][0]==datetime.today().strftime('%Y-%m-%d'):      
    # (Fix: store data in CSV file)
    driver = webdriver.Chrome()
    for lis in links:
        name = lis[0]
        link = lis[1]
        driver.get(link)
        priceStr = driver.find_element(By.XPATH,
                                    "//*[@id=\"corePriceDisplay_desktop_featur"
                                    "e_div\"]/div[1]/span[3]/span[2]/span[2]").text
        price = int(priceStr.replace(',',''))
        data.append([name, price, datetime.today().strftime('%Y-%m-%d')])


def writeData():
    if lastUpdatedDate != datetime.today().strftime('%Y-%m-%d'):
        with open('data.csv', 'w', newline='') as dataFile:
            write = csv.writer(dataFile)
            for row in data:
                write.writerow(row)
    else:
        print("Data is Up-to-date!")



def printData():
    print("\n\nThis is printed data from csv file")
    with open('data.csv', 'r') as dataFile:
        read = csv.reader(dataFile)
        for row in read:
            print(row)
    print("\n\n")


checkPrice()
writeData()
printData()
