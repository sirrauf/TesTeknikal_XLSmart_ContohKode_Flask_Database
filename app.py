from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRETKEY')


def konek_db():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def input_data():
    return render_template('input_data.html', title="Input Data Web")


@app.route('/insert', methods=['POST'])
def insert_db():
    koneksi_db = None
    cursor_db = None
    try:
        koneksi_db = konek_db()
        cursor_db = koneksi_db.cursor()

        querysql = """
        INSERT INTO tbl_user (IDUser, nama_User, Email, password)
        VALUES (%s, %s, %s, %s)
        """

        cursor_db.execute(querysql, (
            request.form['IDUser'],
            request.form['nama_User'],
            request.form['Email'],
            request.form['password']
        ))

        koneksi_db.commit()

        return 'Data berhasil ditambahkan'

    except Exception as e:
        return str(e)

    finally:
        if cursor_db:
            cursor_db.close()
        if koneksi_db:
            koneksi_db.close()
            
@app.route('/lihatdata', methods=['GET'])
def lihat_data():
    koneksi_db = None
    cursor_db = None
    try:
        koneksi_db = konek_db()
        cursor_db = koneksi_db.cursor()

        querysql = """
        SELECT * FROM tbl_user
        """

        cursor_db.execute(querysql)
        data_user = cursor_db.fetchall()

        return render_template('lihat_data.html', data_user=data_user)

    except Exception as e:
        return str(e)

    finally:
        if cursor_db:
            cursor_db.close()
        if koneksi_db:
            koneksi_db.close()


if __name__ == '__main__':
    port_server = int(os.getenv('PORT', 5000))
    app.run(host='127.0.0.1', port=port_server, debug=True)