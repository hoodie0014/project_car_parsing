import pymysql
from Car import Car

class MySQL:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = '60ilya',
            password = 'Sokola042174!',
            database = 'carsdatabase',
            cursorclass=pymysql.cursors.DictCursor
        )
        
    def add(self, cars: list[Car]):
        for car in cars:
            insert_query = "INSERT INTO cars (url_photo, name, price, engine, transmission, drive, body_type, color, mileage, wheel, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (car.url_photo, car.name, car.price, car.engine, car.transmission, car.drive, car.body_type, car.color, car.mileage, car.wheel, car.url))
                self.connection.commit()
                print(f"[INFO] Database: added {car.name}")
    
    def delete_duplicates(self):
        delete_query = "DELETE c1 FROM cars c1 JOIN cars c2 ON c1.name = c2.name WHERE c1.id > c2.id;"
        with self.connection.cursor() as cursor:
            cursor.execute(delete_query)
            self.connection.commit()
            print("[INFO] Database: removed duplicate records")