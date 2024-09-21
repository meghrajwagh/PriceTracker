from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime
import csv

today = datetime.today().strftime('%Y-%m-%d')
links: list = [
        ["LOQ_R7_8845HS_4050", "https://amzn.in/d/4NL6AvO", "Amazon"],
        ["KatanaA17_R7_8845HS_4060", "https://amzn.in/d/c4Scwyz", "Amazon"],
        ["KatanaA15_R7_8845HS_4050", "https://amzn.in/d/c6A2Jzh", "Amazon"],
        ["Victus_R7_8845HS_4050", "https://amzn.in/d/46xtM5l", "Amazon"],
        ["TUF-A15_R7_7735HS_4050", "https://amzn.in/d/c39zkX7", "Amazon"],
        ["LOQ_R7_8845HS_4050", "https://dl.flipkart.com/s/pxd95DuuuN", "Flipkart"],
        ["NitroV_R7_7735HS_4050", "https://dl.flipkart.com/s/pE8I3EuuuN", "Flipkart"],
        ["LOQ_R7_7735HS_4050", "https://dl.flipkart.com/s/pEZhrauuuN", "Flipkart"],
        ["LegionSlim5_R7_7840HS_4050", "https://dl.flipkart.com/s/pEAFcauuuN", "Flipkart"],
        ["LOQ_R7_7435HS_4060", "https://dl.flipkart.com/s/pEZZH1uuuN", "Flipkart"]
        ]
data: list  = []
lastUpdatedDate = None

with open('data.csv', 'r') as dataFile:
    read = csv.reader(dataFile)
    for row in read:
        data.append(row)
    lastUpdatedDate = data[-1][2]


def checkPrice():
    driver = webdriver.Chrome()
    for lis in links:
        prdtName = lis[0]
        link = lis[1]
        site = lis[2]
        driver.get(link)
        if site == "Amazon":
            priceStr = driver.find_element(By.XPATH,
                                        "//*[@id=\"corePriceDisplay_desktop_featur"
                                        "e_div\"]/div[1]/span[3]/span[2]/span[2]").text
            price = int(priceStr.replace(',',''))
            data.append([prdtName, price, today, site])
        else:
            priceStr = driver.find_element(By.CLASS_NAME,"CxhGGd").text
            price = int(priceStr.replace('₹','').replace(',',''))
            data.append([prdtName, price, today, site])


def writeData():
        with open('data.csv', 'w', newline='') as dataFile:
            write = csv.writer(dataFile)
            for row in data:
                write.writerow(row)




def printData():
    print("\n\nThis is printed data from csv file\n")
    with open('data.csv', 'r') as dataFile:
        read = csv.reader(dataFile)
        for row in read:
            print(row)
    print("\n\n")

def forceWrite():
    print("Data is Up-to-date!\n",
          "Do you still want to force write?"
          )
    fWrite = input("y/n?").capitalize()
    if fWrite == "Y":
        writeData()
        print("Force Updated Data Successfully")
    elif fWrite ==  "N":
        pass
    else:
        print("Invalid Input!")
        forceWrite()

def mainMenu():
    print(" 1. Check Price\n",
          "2. Show Previous data\n",
          "3. Update Data\n",
          "0. Exit\n"
          )
    opt = int(input("Enter Option: "))
    if opt == 1:
        checkPrice()
        mainMenu()
    elif opt == 2:
        printData()
        mainMenu()
    elif opt == 3:
        if lastUpdatedDate != today:
            writeData()
            print("Data Updated Successfully")
            mainMenu()
        else:
            forceWrite()
            mainMenu()
    elif opt == 0:
        print("Exiting Programme")
    else:
        print("Invalid Input\nTry again.\n")
        mainMenu()


mainMenu()
