from flask import Flask, request, jsonify
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
def beranda_api():
    return jsonify({
        'status': 'success',
        'message': 'Selamat datang di API Database MySQL',
        'endpoints': {
            'POST /insert': 'Insert data user baru (gunakan Postman, kirim JSON body)',
            'GET /lihatdata/<IDUser>': 'Lihat data user berdasarkan IDUser'
        }
    }), 200


@app.route('/insert', methods=['POST'])
def insert_db():
    koneksi_db = None
    cursor_db = None
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'status': 'error',
                'message': 'Request body harus berupa JSON. Pastikan Content-Type: application/json'
            }), 400

        required_fields = ['IDUser', 'nama_User', 'Email', 'password']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'status': 'error',
                    'message': f'Field "{field}" wajib diisi'
                }), 400

        koneksi_db = konek_db()
        cursor_db = koneksi_db.cursor()

        querysql = """
        INSERT INTO tbl_user (IDUser, nama_User, Email, password)
        VALUES (%s, %s, %s, %s)
        """

        cursor_db.execute(querysql, (
            data['IDUser'],
            data['nama_User'],
            data['Email'],
            data['password']
        ))

        koneksi_db.commit()

        return jsonify({
            'status': 'success',
            'message': 'Data berhasil ditambahkan',
            'data': {
                'IDUser': data['IDUser'],
                'nama_User': data['nama_User'],
                'Email': data['Email']
            }
        }), 201

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

    finally:
        if cursor_db:
            cursor_db.close()
        if koneksi_db:
            koneksi_db.close()


@app.route('/lihatdata/<IDUser>', methods=['GET'])
def lihat_data(IDUser):
    koneksi_db = None
    cursor_db = None
    try:
        koneksi_db = konek_db()
        cursor_db = koneksi_db.cursor()

        querysql = """
        SELECT nama_User, Email, password FROM tbl_user WHERE IDUser = %s
        """

        cursor_db.execute(querysql, (IDUser,))
        data_user = cursor_db.fetchone()

        if data_user:
            return jsonify({
                'status': 'success',
                'data': {
                    'nama_User': data_user['nama_User'],
                    'Email': data_user['Email'],
                    'password': data_user['password']
                }
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': f'User dengan IDUser "{IDUser}" tidak ditemukan'
            }), 404

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

    finally:
        if cursor_db:
            cursor_db.close()
        if koneksi_db:
            koneksi_db.close()


if __name__ == '__main__':
    port_server = int(os.getenv('PORT', 5000))
    app.run(host='127.0.0.1', port=port_server, debug=True)
