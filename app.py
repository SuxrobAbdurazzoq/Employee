from flask import Flask, app
import pymysql


def get_connection():
    return pymysql.connect(
        host='localhost',
        database='hodim_db',
        user='root',
        password='abdurazzokov')

def hodimlarni_oqi():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM hodimlar")
            rows = cursor.fetchall()
            return rows

def hodimni_oqi(id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM hodimlar WHERE id = %s", (id,))
            rows = cursor.fetchone()
            return rows

def hodimni_ochir(id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM hodimlar WHERE id = %s", (id,))
            conn.commit()
              
def hodimni_ozgartir(id, ism, familiya, lavozim, yoshi, jinsi):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE hodimlar SET ism=%s, familiya=%s, lavozim=%s, yoshi=%s, jinsi=%s WHERE id=%s", (ism, familiya,lavozim,yoshi,jinsi, id,))
            conn.commit()

def hodimni_qoshish(ism, familiya, lavozim, yoshi, jinsi):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO hodimlar(ism, familiya, lavozim, yoshi, jinsi) VALUES (%s, %s, %s, %s, %s)", (ism, familiya, lavozim, yoshi, jinsi))
            conn.commit()

app = Flask("test")

@app.route('/delete/<int:id>')
def delete(id):
    pass

@app.route('/insert', methods=['POST'])
def insert():
    pass

@app.route('/update/<int:id>', methods=['GET'])
def update(id):
    pass

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    pass


@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    # app.run(debug=True)
    print("Hello, World!")
    print("Pul qani")
    print("qib boldizmi hamidullo")
    print("dsfwerfgref")
    # hodimni_qoshish("Ali", "Aliyev", "Dasturchi", 25, True)
    # print(hodimlarni_oqi())
    # hodimni_ozgartir(1, "Vali", "Aliyev", "Dasturchi", 25, True)
    # print(hodimlarni_oqi())
    # hodimni_ochir(1)
    # print("====")
    # print(hodimlarni_oqi())
