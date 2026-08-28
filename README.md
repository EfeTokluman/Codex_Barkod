# Codex_Barkod
Bu Uygulama Amacı Personelin Ve Denetimin Çok Olması Gereken Yerlerde Kunlanılan Programlar Çoğunlukla Abonelik Sistemli Olduğundan Ben Bu Uygulamayı Yapmaya Karar Verdim

Uygulamada İş Oluştura Bilir Personel Hesabı Açarak Ona İş ataya Bilir Ve İşlerinizi Numaralandıra Bilirsiniz

Şu Anda Sadece Sunucu Tarafını Yazdımki Oda Tam Değil

NOT:Güvenlk testleri Sadece ai yaptırılmıştır bütün program kendim yazdım
2 NOT:Bu Uygulama Sadece Local Ağlarda Çalıştırılmak İçin Yapılmıştır Ama İllaki Ben 2 3 Yeri Bağlamak İstiyorsanızda Tailscale Gibi Şifreli Tünelden Geçirirseniz Sorun Muhtemelen Olma   
YASAL UYARI: Projeden Kaynaklı Ola Bilicek Hiçbir Zararın Sorumluluğunu Almıyorum Bu Proje Sadece Bir Hobi Projesidir.

Chat Gpt Tarafından Yapılan Güvenlik Testleri:

## 🔐 Güvenlik

**Codex Secure Server 1.0**, çeşitli kimlik doğrulama, yetkilendirme ve API güvenliği senaryolarına karşı **OpenAI tarafından geliştirilen ChatGPT'nin desteğiyle** test edilmiştir.

### 🤖 ChatGPT Destekli Güvenlik Testleri

Özel güvenlik test senaryoları ve test araçları **ChatGPT (OpenAI)** ile birlikte hazırlanmış ve yerel geliştirme sunucusunun authentication, authorization, token yönetimi ve API davranışlarını değerlendirmek için kullanılmıştır.

### 🧪 Test Sonuçları

| Test                                      |     Sonuç     |
| ----------------------------------------- | :-----------: |
| 🔑 Yetki Yükseltme (Privilege Escalation) | ✅ TESTİ GEÇTİ |
| 👤 Rol Manipülasyonu                      | ✅ TESTİ GEÇTİ |
| 🎫 Token Manipülasyonu                    | ✅ TESTİ GEÇTİ |
| 💉 SQL Injection                          | ✅ TESTİ GEÇTİ |
| 🔓 Login Bypass                           | ✅ TESTİ GEÇTİ |
| 🌐 HTTP Method Bypass                     | ✅ TESTİ GEÇTİ |
| 🧪 Input Fuzzing                          | ✅ TESTİ GEÇTİ |
| 🛡️ API Yetkilendirmesi                   | ✅ TESTİ GEÇTİ |
| 🔁 Duplicate Parametre Testleri           | ✅ TESTİ GEÇTİ |
| 🎯 Yetkisiz Kullanıcı Hedefleme           | ✅ TESTİ GEÇTİ |

### 📌 Test Ortamı

**Hedef:** `127.0.0.1:8000`
**Ortam:** Yerel geliştirme sunucusu
**Güvenlik Test Desteği:** **ChatGPT (OpenAI)**

> ⚠️ **Güvenlik Notu:** Bu testlerin geçilmiş olması, yazılımın tamamen güvenli veya kırılamaz olduğu anlamına gelmez. Sonuçlar yalnızca gerçekleştirilen test senaryolarını kapsamaktadır.

