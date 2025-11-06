from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Car import Car

def parse(driver: Chrome):
    cars = []
    for page in range(1, 5):
        
        driver.get(f"https://www.avito.ru/vladivostok/avtomobili?radius=200&searchRadius=200&p={page}")
        
        try:
            urls = []
            
            list_cars = driver.find_elements(By.XPATH, '//a[@data-marker="item-title"]')
            
            for el in list_cars:
                urls.append(el.get_attribute('href'))
        except Exception as ex:
            print(ex)
        
        for url in urls:
            car = Car()
            
            driver.get(url)
            
            try:
                car.name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[6]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[1]/h1').text
            except Exception as ex:
                print(ex)
                
            try:
                car.price = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[6]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div/span/span/span[1]').text
            except Exception as ex:
                print(ex)
                
            try:
                car.url_photo = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[6]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div[3]/img').get_attribute("src")
            except Exception as ex:
                print(ex)
            
            try:
                car.url = driver.current_url
            except Exception as ex:
                print(ex)
                
            try:
                table = driver.find_element(By.XPATH, '//div[@data-marker="item-view/item-params"]').text.split('\n')
                for el in table:
                        if "Тип двигателя: " in el:
                            car.engine = el.replace("Тип двигателя: ", "")
                        elif "Коробка передач: " in el:
                            car.transmission = el.replace("Коробка передач: ", "")
                        elif "Привод: " in el:
                            car.drive = el.replace("Привод: ", "")
                        elif "Тип кузова: " in el:
                            car.body_type = el.replace("Тип кузова: ", "")
                        elif "Цвет: " in el:
                            car.color = el.replace("Цвет: ", "")
                        elif "Пробег: " in el:
                            car.mileage = el.replace("Пробег: ", "")
                        elif "Руль: " in el:
                            car.wheel = el.replace("Руль: ", "")
            except Exception as ex:
                print(ex)
                
            cars.append(car)
            print(f"[INFO] Avito: added {car.name}")
        
    return cars