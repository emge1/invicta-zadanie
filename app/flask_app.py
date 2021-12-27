from flask import Flask, Response
import sqlite3

app = Flask(__name__)


@app.route("/")
def main_page():
    return '''<html><body> Dzień dobry. Aby pobrać plik .csv z danymi, proszę kliknąć 
    <a href="/app/users_todos">tutaj</a>. </body></html>'''


@app.route("/app/users_todos")
def get_users_todos():
    con = sqlite3.connect('../app/database.db')
    cur = con.cursor()
    req = '''SELECT u.name, u.address_city AS city, t.title, t.completed FROM users u JOIN todos t WHERE
     u.id = t.userId GROUP BY t.id'''
    cur.execute(req)
    con.commit()
    data = cur.fetchall()
    headers = 'name, city, title, completed\n'
    output = headers
    for tup in data:
        output += tup[0] + ', ' + tup[1] + ', ' + tup[2] + ', ' + tup[3] + '\n'

    return Response(output, mimetype="text/csv",
                    headers={"Content-disposition": "attachment; filename=users_todos.csv"})


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)