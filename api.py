import requests

token = 0

def ayarla(url):
    global url_sunucu
    url_sunucu = url

def baglan():
    bir = requests.get(url_sunucu)
    json = bir.json()
    if json["api_version"] == "CBS_3.0":
        print("Eşleşme Tamamlandı Sunucu Uyumlu")
        print(json)
        login("root","codex_barkod+123")
    else:
        print("Sunucu Versiyonları uyuşmuyor!")
        print(json)

ayarla("http://127.0.0.1:8000/")

def login(kunlanıcı_adı,şifre):
    global token

    login_istek = requests.post(url_sunucu + "login",params={
        "username":kunlanıcı_adı,"password":şifre
    })
    print(login_istek)
    json_login = login_istek.json()
    try:
        token = json_login["token"]
        print(json_login)
        print(token)
        is_al()
        is_create("test from api","1","?")
        user_create("test_admin","test_admin","admin")
    except:
        print("Hata!")
        print(json_login)



def is_al():
    is_istek = requests.get(url_sunucu + "jobs",params={
        "token":token
    })
    is_istek_json = is_istek.json()
    print(is_istek_json)

def is_create(title,kime,files):
    is_create_istek = requests.post(url_sunucu + "jobs",params={
        "title":title,"kime":kime,"files":files,"token":token
    })
    is_create_json = is_create_istek.json()
    print(is_create_json)

def user_create(username,password,role):
    create_user = requests.post(url_sunucu + "users/create",params={
        "username":username,"password":password,"token":token,"role":role
    })
    create_user_json = create_user.json()
    print(create_user_json)

def user_delete(username):
    delete_user = requests.post(url_sunucu + "users/delete",params={
        "username":username,"token":token
    })
    delete_user_json = delete_user.json()
    print(delete_user_json)

#baglan() #Api Test İçin Burayı Etkinleştirin Ve baglan fonkiyonundaki hesap bilgilerini girin
