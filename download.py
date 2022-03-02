from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os


start_time = time.time()

# Add your credentials
EMAIL = ""
PASS = ""

"""
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', os.getcwd)
"""
fireFoxOptions = webdriver.FirefoxOptions()
#fireFoxOptions.add_experimental_option("prefs", profile) 
#fireFoxOptions.headless = True
profile = webdriver.FirefoxProfile()
#profile.set_preference("browser.download.folderList", 2)
#profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.useDownloadDir", True)
print(os.getcwd())
profile.set_preference("browser.download.dir", os.getcwd())
#profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
#fireFoxOptions.setProfile(profile)
driver = webdriver.Firefox(firefox_profile=profile,options=fireFoxOptions)
driver.set_page_load_timeout(25)
driver.get("https://iris.science-it.ch/")
#assert "Python" in driver.title
"""
elem = driver.find_element_by_name("cookiescript_accept")
elem.clear()

elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
"""
ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    #print ii.tag_name
    print(ii.get_attribute('id'))

elem = driver.find_element(by=By.ID,value="cookiescript_accept")
elem.click()

elem2 = driver.find_element(by=By.ID,value="top-navigation")
button = elem2.find_element_by_xpath(".//p[@class='navbar-btn']")
button.click()

time.sleep(1)
elem3 = driver.find_element(by=By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/input")
#time.sleep(10)
#email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]/div[1]/input"))).get_attribute("value")
#print(elem3.find_element_by_xpath(".//span[@class='input-group-addon']").text)
#print(elem3.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[1]/input").text)

elem3.send_keys(EMAIL)
#elem3.submit()

login_butt = driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary")
login_butt.click()

time.sleep(1)
pass_elem = driver.find_element(by=By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/input")
pass_elem.send_keys(PASS)
#pass_elem.submit()

login_butt = driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary")
login_butt.click()



time.sleep(2)

admin_tab = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/div/div[2]/div/ul/li[5]/span[2]")
print(admin_tab.text)
admin_tab.click()

bookings_tab = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div[5]/div/div/ul/li[4]/span[2]")
print(bookings_tab.text)
bookings_tab.click()

time.sleep(5)

select_all = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div[5]/div/div/div[4]/div/div[2]/div[2]/div/admin-bookings-list/div/div[2]/div[2]/a[2]")
print(select_all.text)
select_all.click()


#val = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "a5dc26a2-b819-4c29-899d-44470e302f2c"))).get_attribute("value")

#select = Select(driver.find_element_by(by=By.CSS_SELECTOR,'#f41826be-980c-425c-8c9b-f62031d380e7'))
#select = Select(driver.find_element(by=By.XPATH,value="//span[contains(input class, 'k-dropdown')]"))
#select.select_by_visible_text('Export to Excel')
dropdown = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/div/div[2]/div/div[5]/div/div/div[4]/div/div[2]/div[2]/div/admin-bookings-list/div/div[2]/div[2]/span[1]")
button  = dropdown.find_element_by_xpath(".//span[@class='k-input']")
button.click()


export = driver.find_element(by=By.XPATH,value="/html/body/div[218]/div/div[2]/ul/li[4]")
export.click()
time.sleep(1)
action_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div/div[5]/div/div/div[4]/div/div[2]/div[2]/div/admin-bookings-list/div/div[2]/div[2]/span[2]/a")
print(action_button.text)
action_button.click()

time.sleep(1)




"""
ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    #print ii.tag_name
    print(ii.get_attribute('id'))
"""
driver.close()

print("Script executed in ", time.time()-start_time, " secs")

