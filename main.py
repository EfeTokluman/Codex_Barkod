from fastapi import FastAPI
import sqlite3
import random
import hashlib

create_admin = False

app = FastAPI()
def init_db():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       title TEXT NOT NULL,
       status TEXT DEFAULT 'beklemede',
       kime TEXT DEFAULT '0',
       files TEXT DEFAULT ''
       )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT NOT NULL UNIQUE,
       password TEXT NOT NULL,
       role TEXT NOT NULL DEFAULT 'user',
       token TEXT
       )
    """)
    conn.commit()
    conn.close()
    print("database OK")

init_db()

@app.post("/users/create")
def create_user(username: str, password: str,token: int, role: str = "user",):
    try:
        token_ok(token,"admin")
    except Exception:
        return {"error":"Giriş Başarısız Database RET Verdi Hata Kodu:403"}
    password = hashla(password)
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password ,role)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return {"error":"Bu Kunlanıcı Adı Zaten Var"}
    conn.close()
    return {"message": "Kunlanıcı Eklendi","username": username, "role": role}

@app.post("/users/delete")
def delete_user(username:str ,token: int):
    try:
        token_ok(token,"admin") #burası tokeni yetkilendirme/ret yeri
    except Exception:
        print("UYARI! YETKİSİZ KUNLANICI SİLİNME GİRİŞİMİ!")
        print(f"Deneyen Kunlanıcı Tokeni:{token}")
        return {"error":"Hata Kodu:403 Bu Eylem Kayıt Altına Alındı Ve Bildirilicek."}

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM users WHERE username = ?",
            (username,)
        )
        conn.commit()
        conn.close()
        print(f"Token:{token} Kunlanılarak Şu Kunlanıcı Silindi:{username}")
        return {"message":"Kunlanıcı Başarıyla Silindi"}
    except:
        return {"error":"Kunlanıcı Belirlenmeyen Hatadan Dolayı Silinemedi"}

@app.post("/login")
def login(username:str,password:str):
    password = hashla(password)
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, role FROM users WHERE username = ? AND password = ?",
        (username,password)
    )
    row = cursor.fetchone()
    if row is None:
        return {"error":"403 - Giriş REDDEDİLDİ"}
    token = random.randint(10000000, 99999999)
    token_db = hashla(token)
    cursor.execute(
        "UPDATE users SET token = ? WHERE id = ?",
        (token_db, row[0])
    )
    conn.commit()
    conn.close()
    return {"message":"Giriş OK","user_id": row[0], "role": row[1],"token":token}

@app.get("/")
def read_root():
    return{"api_version":"CBS_2.3","api_version_human":"Codex Barkod Sunucusu 2.3"}

@app.get("/jobs")
def get_jobs(token:int):
    try:
        user_id , role =token_ok(token,"user")
    except Exception:
        return {"error":"Giriş Başarısız Database RET Verdi Hata Kodu:403"}

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    try:
        if role == "admin":
            cursor.execute("SELECT id,title,status,kime,files FROM jobs")
        else:
            cursor.execute("SELECT id, title ,status ,kime,files FROM jobs WHERE kime = ?", (str(user_id),))
    except sqlite3.OperationalError as hata:
        return {"error":"Arama Sorgusu Başarısız","hata_kodu":hata}
    rows = cursor.fetchall()
    conn.close()


    jobs = []
    for r in rows:
        dosya_liste= r[4].split(",") if r[4] else []
        jobs.append({
            "id": r[0],
            "title": r[1],
            "status": r[2],
            "kime": r[3],
            "files": dosya_liste
        })
    return jobs

@app.post("/jobs")
def create_job(title: str,kime: str,files:str,token:int):
    try:
        user_id,role = token_ok(token,"user")
    except Exception:
        return {"error":"Giriş Başarısız Database RET Verdi Hata Kodu:403"}

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jobs (title,kime,files) VALUES (?,?,?)", (title,kime,files))
    conn.commit()
    conn.close()
    return {"message": "İş Eklendi","title:": title}


def token_ok(token,gerekli_rol):
    token = hashla(token)
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, role FROM users WHERE token = ?",
        (token,)
    )
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise Exception("ret - token hatası!")
    else:
        user_id, role = row
        if "admin" == role: # admin yetkisi en üste
            return user_id,role
        if gerekli_rol == role:
            return user_id,role
        else:
            raise Exception("ret - rol hatası!")

def create_admin_user():
    if create_admin == True:
        conn = sqlite3.connect("jobs.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("root", "codex_barkod+123" ,"admin")
        )
        conn.commit()
        conn.close()
        print("Admin Hesabı Oluşturuldu lütfen admin hesap oluşturmayı kapat ve reboot at!")

def hashla(password):
    sha256password = hashlib.sha256(password.encode()).hexdigest()
    return sha256password


create_admin_user()