#import
from selenium import webdriver

#read a preprocessed file
List = open(r"C:\.........\invoices.txt").readlines()

#set up references
options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")

#create driver
driver = webdriver.Chrome(executable_path=r"C:\...../chromedriver", options=options)

#access database website
driver.get("https://........org/")
UserName = driver.find_element_by_id("UserName")
UserName.send_keys("..........")

Password = driver.find_element_by_id("Password")
Password.send_keys(".........")

driver.find_element_by_id("submitbtn").click()

#auto download
for x in range(len(List)):
    print(List[x])
    driver.get(List[x])
