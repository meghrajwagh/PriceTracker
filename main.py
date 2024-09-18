from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


links: dict[str, str] = {"LOQ_R7_8845HS_4050": "https://amzn.in/d/4NL6AvO",
                         "KatanaA17_R7_8845HS_4060": "https://amzn.in/d/c4Scwyz"}
data: dict[str, list] = {"Name": [["Date", "price"]], "LOQ_R7_8845HS_4050": []}
# temp = []


def checkPrice():
    # if data["LOQ_R7_8845HS_4050"][0][0] == datetime.today().strftime('%Y-%m-%d'):      (Fix: store data in CSV file)
    driver = webdriver.Chrome()
    for name in links:
        if name not in data:
            data[name] = []
        driver.get(links[name])
        price = driver.find_element(By.XPATH,
                                    "//*[@id=\"corePriceDisplay_desktop_featur"
                                    "e_div\"]/div[1]/span[3]/span[2]/span[2]")
        data[name].append([price.text, datetime.today().strftime('%Y-%m-%d')])


def printData():
    for name in data:
        print(f"{name}: ", end="")
        for vals in data[name]:
            print(vals)


checkPrice()
printData()
