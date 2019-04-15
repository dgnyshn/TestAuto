from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_argument("--disable-popup-blocking");
opt.add_argument("--disable-notifications");
driver = webdriver.Chrome(chrome_options = opt) # Chrome(/path/to/chromedriver.exe)
driver.get("https://www.onurair.com/tr/")

class testBilet():
   
    def fieldHomepage():
        xpaths = [
            #Nereden
            "//*[@id='depPortArea']/label/span[2]",
            "/html/body/div[4]/div/span/span/ul/li[2]/span/ul/li[4]/span",
            
            #Nereye
            "//*[@id='arrPortArea']/div/label/span[2]",
            "/html/body/div[4]/div/span/span/ul/li[2]/span/ul/li[4]/span",
            #Gidiş
            "//*[@id='departureDate']",
            "/html/body/div[1]/div[1]/table/tbody/tr[5]/td[4]"
        ]
        for path in xpaths:
            driver.find_element_by_xpath(path).click()
        
        
        #Dönüş 
        for i in range(2):
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/thead/tr[1]/th[3]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[5]/td[4]").click()
    
        #Yetişkin
        
        for i in range(2 , 11 , 1): #All options
            driver.find_element_by_xpath("//*[@id='adultArea']/label[2]/span[2]/span[2]").click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[4]/div/span/span/ul/li[{}]/span/span'.format(i)).click()
            time.sleep(1)
      
        driver.find_element_by_xpath("//*[@id='adultArea']/label[2]/span[2]/span[2]").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/span/span/ul/li[2]/span/span").click()

        #Çocuk Option

        for i in range(2 , 11 , 1): #All options
            driver.find_element_by_xpath("//*[@id='childArea']/label[2]/span[2]").click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[4]/div/span/span/ul/li[{}]/span'.format(i)).click()
            time.sleep(1)

        driver.find_element_by_xpath("//*[@id='childArea']/label[2]/span[2]").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/span/span/ul/li[1]/span").click()
       
        #Bebek Option
        for i in range(2 , 11 , 1): #All options
            driver.find_element_by_xpath("//*[@id='infantArea']/label[2]/span[2]/span[1]/span").click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[4]/div/span/span/ul/li[{}]/span'.format(i)).click()
            time.sleep(1)

        driver.find_element_by_xpath("//*[@id='infantArea']/label[2]/span[2]/span[1]/span").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/span/span/ul/li[1]/span").click()
       
        #Submit
        driver.find_element_by_xpath("//*[@id='btnSearch']").click()
        
    def fieldSecondPage():
        
        driver.execute_script("window.scrollTo(0, 500);")  
        driver.find_element_by_xpath("//*[@id='bundleSelectDivId_0_3_0_0']/div[2]").click()
        driver.execute_script("window.scrollTo(0, 500);")
        driver.find_element_by_xpath("//*[@id='bundleSelectDivId_0_3_0_0']/div[2]").click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath("//*[@id='bundleSelectDivId_1_3_0_0']/div[2]").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='btnContinue']").click()
        time.sleep(1)
    
    def fieldInfo():
        
        time.sleep(1)
        driver.find_element_by_xpath('/html/body').click()
        time.sleep(1)
        #Üyeliği test et ----<
        driver.execute_script("window.history.go(-1)")
        driver.find_element_by_id("gender1-selectized").click()
        time.sleep(1)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Ünvan *'])[1]/following::div[4]").click()
        time.sleep(1)
        driver.find_element_by_name("name1").send_keys("Doğanay")
        driver.find_element_by_name('surname1').send_keys("Şahin")

        
        
        driver.find_element_by_id("nationality1-selectized").click() #Uyruk
        time.sleep(1)
        #Select Turkey
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Uyruk *'])[1]/following::div[4]").click()
        time.sleep(2)
        #Birth
        driver.find_element_by_id("bday_day_1-selectized").click() 
        time.sleep(1)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Doğum Tarihi *'])[1]/following::div[4]").click()
        time.sleep(1)
        #Month
        driver.find_element_by_id("bday_month_1-selectized").click() 
        time.sleep(1)
        #Year
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='.'])[1]/following::div[4]").click()
        driver.find_element_by_id("bday_year_1-selectized").send_keys(Keys.ARROW_DOWN , Keys.ENTER)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #Filling the information field
        ids = ["natId1" , "loyalty-tel-number1" ,"frst-tel-number0" , "email0"]
        infos = ["ID Number" , "33333333333" , "Phone Number" , "dgnyshn@gmail.com"]
       
        ###   User spesific infos
        #natId1 must be entered 
        #first-tel-numberm0 must be entered (like 5396662211)

        for i,j in zip(ids,infos):
            driver.find_element_by_id(i).send_keys(j)

        #Optional checkboxes
        #for i in range(2):
           # driver.find_element_by_id('smsCheckLabel').click()
            #time.sleep(3)
        
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        # could not retrive member information from loyalty system for {0} Error
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath('//*[@id="btnSave"]').click()
         # But the second click does not give an Error ? 
        
    def seatSelect():
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 500);")
        driver.find_element_by_xpath('//*[@id="seatMenuOpenLink"]').click()
        driver.execute_script("window.scrollTo(0, 800);")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="SEAT_8A"]').click()
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="SEAT_8B"]').click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 1800);")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="cateringMenuOpenLink"]').click()
        driver.find_element_by_xpath('//*[@id="cateringSelectionBodyDiv"]/div[3]/div/div/div[1]/div/div/div/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="cateringSelectionBodyDiv"]/div[3]/div/div/div[2]/div/div/div/a').click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 2500);")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="baggageMenuOpenLink"]').click()
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='DOĞANAY ŞAHIN'])[2]/following::div[6]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='baggageSelectionBodyDiv']/div[2]/div[1]/div[3]/div/div[2]/div/div[5]/div/div[1]/div").click()
        time.sleep(2)
        driver.find_element_by_link_text("Onayla").click()
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='DOĞANAY ŞAHIN'])[2]/following::div[6]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='baggageSelectionBodyDiv']/div[2]/div[3]/div[3]/div/div[2]/div/div[5]/div/div[1]/div").click()
        driver.find_element_by_link_text("Onayla").click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath("//*[@id='QFTK']/tbody/tr[1]/td/label").click()

        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='addSSRContinueBTn']").click()
    
    


if __name__ == "__main__":
    testBilet.fieldHomepage()
    time.sleep(1)
    testBilet.fieldSecondPage()
    time.sleep(1)
    testBilet.fieldInfo()
    time.sleep(1)
    testBilet.seatSelect()
    time.sleep(1)
    driver.close()