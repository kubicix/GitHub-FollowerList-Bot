from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# if you want signIn() method to work you have to fill the blanks 
# anyway bot can work without logging in . it's just an add on
username = ""
password = ""

# The username of the person you want to get the follower list
# For the program to work you have to fill the person string with person's username

person="kubicix"


class Github:
    def __init__(self,username,password) -> None:
        self.browser = webdriver.Edge("advanced-modules/msedgedriver.exe")
        self.username=username
        self.password=password
        self.followers = []
    
    def loadFollowers(self):
        names=self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
        for n in names:
            self.followers.append(n.find_element(By.CSS_SELECTOR,"span.Link--secondary").text)

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        
        username=self.browser.find_element(By.XPATH,"//*[@id='login_field']")
        password=self.browser.find_element(By.XPATH,"//*[@id='password']")

        username.send_keys(self.username)
        password.send_keys(self.password)

        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[11]").click()

    def getFollowers(self):
        # You can modify string manually here
        self.browser.get(f'https://github.com/{person}?tab=followers')
        time.sleep(2)
        self.loadFollowers()

        if(len(github.followers)<50):
            pass

        else:
            while True:
                try:
                    links =self.browser.find_element(By.CSS_SELECTOR,"div.paginate-container").find_elements(By.TAG_NAME,"a")
                    

                    if len(links)==1:
                        if links[0].text=="Next":
                            links[0].click()
                            time.sleep(1)
                            self.loadFollowers()
                            
                        else:
                            break
                    else:
                        for link in links:
                            if link.text=="Next":
                                
                                link.click()
                                time.sleep(1)
                                self.loadFollowers()
                            else:
                                continue
                except:
                    self.loadFollowers()
                
            


                    

github =Github(username,password)

github.signIn()
github.getFollowers()
print(github.followers)
print("Follower Count: ",len(github.followers))
github.browser.close()
