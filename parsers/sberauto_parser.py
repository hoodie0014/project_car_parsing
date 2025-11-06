from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Car import Car

def parse(driver: Chrome):
    cars = []
    for page in range(1, 16):
        driver.get(f"https://sberauto.com/cars/used?page={page}")
        
        try:
            urls = []
            cars_list = driver.find_elements(By.CLASS_NAME, "jss188")
            
            for cars_ in cars_list:
                urls.append(cars_.get_attribute('href'))
        except Exception as ex:
            print(ex)
        
        for url in urls:
            car = Car()
            
            driver.get(url)
            
            try:
                car.name = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/section/div[2]/h1').text
            except Exception as ex:
                print(ex)
                
            try:
                car.price = driver.find_element(By.XPATH, '//p[@data-testid="autoPrice"]    ').text
            except Exception as ex:
                print(ex)
                
            try:
                car.url_photo = driver.find_element(By.XPATH, '//img[@data-test-id="first_photo_start"]').get_attribute('src')
            except Exception as ex:
                print(ex)
                
            try:
                car.url = driver.current_url
            except Exception as ex:
                print(ex)
                
            try:
                car.body_type = driver.find_element(By.XPATH, '//p[@data-test-id="bodyType"]').text
            except Exception as ex:
                print(ex)
                
            try:
                car.color = driver.find_element(By.XPATH, '//p[@data-test-id="color"]').text
            except Exception as ex:
                print(ex)
                
            try:
                car.mileage = driver.find_element(By.XPATH, '//p[@data-test-id="mileage"]').text
            except Exception as ex:
                print(ex)
                
            try:
                car.engine = driver.find_element(By.XPATH, '//p[@data-test-id="engineType"]').text
            except Exception as ex:
                print(ex)
                
            try:
                car.transmission = driver.find_element(By.XPATH, '//p[@data-test-id="transmission"]').text
            except Exception as ex:
                print(ex)
                
            try:
                car.wheel = driver.find_element(By.XPATH, '//p[@data-test-id="wheel"]').text
            except Exception as ex:
                print(ex)
                
            try:
                car.drive = driver.find_element(By.XPATH, '//p[@data-test-id="transmissionDrive"]').text
            except Exception as ex:
                print(ex)
            
            cars.append(car)
            print(f"[INFO] SberAuto: added {car.name}")
        
    return cars
    
