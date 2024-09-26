import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automation.credence.in/")
driver.find_element(By.LINK_TEXT, "Login").click()
# Enter EMAIL ID
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")
# Enter password using CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")
# Click on login button
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
# Click on product-->Apple Macbook Pro
driver.find_element(By.XPATH, "//h3[normalize-space() ='Apple Macbook Pro']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# click continue shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
# Click on product-->Apple iPad Retina
driver.find_element(By.XPATH, "//h3[normalize-space() ='Apple iPad Retina']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# click continue shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
# Click on product-->Apple iPad Retina
driver.find_element(By.XPATH, "//h3[normalize-space() ='Headphones']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
#

q1 = driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr[1]/td[3]/select')
ele = Select(q1).select_by_index(1)

q2 = driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr[2]/td[3]/select')
ele2 = Select(q2).select_by_index(2)

driver.implicitly_wait(10)
q3 = driver.find_element(By.XPATH,
                         '/html/body/div/table/tbody/tr[3]/td[3]/select[1]')  # here element gives stale element exception,solutions-use wait,try and except and use refresh
ele3 = Select(q3).select_by_index(4)

l = driver.find_elements(By.CSS_SELECTOR, "tbody tr")                         #since this would be list it should be elements and not element other wise throughs error

price_lst = []
for r in range(1, len(l) - 2):
    var = driver.find_element(By.CSS_SELECTOR, 'tbody tr:nth-child(' + str(r) + ') td:nth-child(4)').text  # here $2000
    var2 = (var[1:])  # here 2000 at same time and then stored in list
    print(var2)
    price_lst.append(var2)

exp_sum_amount = round(sum(price_lst), 2)



# var2 = sum(Price_List)
# Exp_SubTotal = round(var2, 2)
# # print(Exp_SubTotal)





# for r in range(1, l - 2):
#     Var = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
#     Product_Price = (Var[1:])     #this is to remove initial symbol and then to add it to list $2299.99 to 2299.99
#     print(Product_Price)

