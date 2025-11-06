from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

# Конфигурация базы данных
db = MySQLdb.connect(user='60ilya', passwd='Sokola042174!', db='carsdatabase', host='localhost')

@app.route('/')
def index():
    cursor = db.cursor()
    query = "SELECT * FROM cars"
    cursor.execute(query)
    cars = cursor.fetchall()
    return render_template('index.html', cars=cars)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_query = request.form.get('search_query')
    sort_by = request.form.get('sort_by')
    sort_order = request.form.get('sort_order')
    cursor = db.cursor()
    
    query = "SELECT * FROM cars WHERE name LIKE %s"
    params = [f'%{search_query}%']
    
    if sort_by:
        query += f" ORDER BY {sort_by}"
        if sort_order == 'desc':
            query += " DESC"
    
    cursor.execute(query, params)
    cars = cursor.fetchall()
    return render_template('search_results.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)