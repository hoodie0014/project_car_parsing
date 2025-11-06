from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Car import Car

def parse(driver: Chrome):
    cars = []
    
    for page in range(1, 11):
        driver.get(f"https://auto.drom.ru/region25/all/page{page}/")
        
        try:
            urls = []
            
            list_cars = driver.find_elements(By.XPATH, '//a[@data-ftid="bulls-list_bull"]')
            
            for el in list_cars:
                urls.append(el.get_attribute('href'))
                    
        except Exception as ex:
            print(ex)
            
        for url in urls:
            car = Car()

            driver.get(url)
            
            try:
                car.name = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/h1/span').text
            except Exception as ex:
                print(ex)
                
            try:
                car.price = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]').text
            except Exception as ex:
                print(ex)
            
            try:
                car.url_photo = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/a').get_attribute('href')
            except Exception as ex:
                print(ex)
                
            try:
                car.url = driver.current_url
            except Exception as ex:
                print(ex)
            
            try:   
                table = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/table').text.split('\n')
                for el in table:
                    if "Двигатель " in el:
                        car.engine = el.replace("Двигатель ", "")
                    elif "Коробка передач " in el:
                        car.transmission = el.replace("Коробка передач ", "")
                    elif "Привод " in el:
                        car.drive = el.replace("Привод ", "")
                    elif "Тип кузова " in el:
                        car.body_type = el.replace("Тип кузова ", "")
                    elif "Цвет " in el:
                        car.color = el.replace("Цвет ", "")
                    elif "Пробег " in el:
                        car.mileage = el.replace("Пробег ", "")
                    elif "Руль " in el:
                        car.wheel = el.replace("Руль ", "")
            except Exception as ex:
                print(ex)
                
            cars.append(car)
            print(f"[INFO] Drom: added {car.name}")
        
    return cars