---
# Test Teknikal XL Smart – Contoh Kode Python Flask Database
---

## Requirements

1. Download & Install Python (minimal versi 3.10.11)
   [https://www.python.org/downloads/release/python-31011/](https://www.python.org/downloads/release/python-31011/)

2. Buat virtual environment:

   ```bash
   python -m venv venv
   ```

3. Aktifkan virtual environment (Windows):

   ```bash
   venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Menjalankan Web Server

Jalankan perintah berikut di Command Prompt (CMD) pada folder project:

```bash
flask run
```

atau

```bash
python app.py
```

Server akan berjalan di `http://127.0.0.1:5000`

---

## Cara Menggunakan API dengan Postman

### 1. Halaman Utama

| Item   | Detail                   |
| ------ | ------------------------ |
| Method | `GET`                    |
| URL    | `http://127.0.0.1:5000/` |

Menampilkan daftar endpoint yang tersedia.

---

### 2. Insert Data User

| Item         | Detail                         |
| ------------ | ------------------------------ |
| Method       | `POST`                         |
| URL          | `http://127.0.0.1:5000/insert` |
| Content-Type | `application/json`             |

![SS_POST_POSTMAN](https://raw.githubusercontent.com/sirrauf/TesTeknikal_XLSmart_ContohKode_Flask_Database/main/SS_Hasil_POSTMAN/SS_POST_POSTMAN.png)

**Langkah di Postman:**

1. Pilih method **POST**
2. Masukkan URL `http://127.0.0.1:5000/insert`
3. Buka tab **Headers**, tambahkan:
   - Key: `Content-Type`
   - Value: `application/json`
4. Buka tab **Body** → pilih **raw** → pilih **JSON**
5. Masukkan JSON berikut:

```json
{
  "IDUser": "2",
  "nama_User": "Rauf",
  "Email": "sirrauf@gmail.com",
  "password": "123456"
}
```

**Contoh Response (201 Created):**

```json
{
  "status": "success",
  "message": "Data berhasil ditambahkan",
  "data": {
    "IDUser": "2",
    "nama_User": "Rauf",
    "Email": "sirrauf@gmail.com"
  }
}
```

---

### 3. Lihat Data User berdasarkan IDUser

| Item   | Detail                                     |
| ------ | ------------------------------------------ |
| Method | `GET`                                      |
| URL    | `http://127.0.0.1:5000/lihatdata/{IDUser}` |

![SS_GET_POSTMAN](https://raw.githubusercontent.com/sirrauf/TesTeknikal_XLSmart_ContohKode_Flask_Database/main/SS_Hasil_POSTMAN/SS_GET_POSTMAN.png)

**Langkah di Postman:**

1. Pilih method **GET**
2. Masukkan URL, contoh: `http://127.0.0.1:5000/lihatdata/2`

**Contoh Response (200 OK):**

```json
{
  "status": "success",
  "data": {
    "nama_User": "Rauf",
    "Email": "sirrauf@gmail.com",
    "password": "123456"
  }
}
```

**Jika IDUser tidak ditemukan (404 Not Found):**

```json
{
  "status": "error",
  "message": "User dengan IDUser \"99\" tidak ditemukan"
}
```
