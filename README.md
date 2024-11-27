# Baykar Personel Uygulaması

Django tabanlı, uçak parçalarını, stok seviyelerini ve envanter verilerini yönetmek için geliştirilmiş bir sistem.

## Özellikler
- **Envanter Yönetimi**: Parçaları detaylı bilgilerle ekleyin, görüntüleyin ve yönetin.
- **Kullanıcı Doğrulama**: Envanter yönetimi için güvenli erişim.
- **Duyarlı Tasarım**: Modern bir arayüz için Bootstrap entegrasyonu.

## Kullanılan Teknolojiler
- **Backend**: Django, Django Rest Framework
- **Veritabanı**: PostgreSQL
- **Frontend**: Bootstrap (Django şablonlarında)
- **Containerizasyon**: Docker, Docker Compose

## Kurulum ve Başlangıç

### Gereksinimler
- Docker ve Docker Compose kurulu olmalıdır.

### Adımlar
1. Depoyu klonlayın:
   - Bir terminal açarak şu komutları çalıştırın:
     ```bash
     git clone https://github.com/your-username/baykar-inventory.git
     cd baykar-inventory
     ```

2. Servisleri oluşturun ve başlatın:
   - Terminalde şu komutu çalıştırın:
     ```bash
     docker-compose up --build
     ```
   - Bu komut şunları yapacaktır:
     - PostgreSQL veritabanını kurar.
     - Migrations işlemlerini uygular.
     - Varsayılan başlangıç verilerini yükler.
     - Django geliştirme sunucusunu başlatır.

3. Uygulamaya erişin:
   - Tarayıcınızdan aşağıdaki adreslere gidin:
     - **API ve Yönetici Paneli**: [http://localhost:8000](http://localhost:8000)
     - **PgAdmin**: [http://localhost:5050](http://localhost:5050)
       - Varsayılan giriş bilgileri:
         - E-posta: `admin@admin.com`
         - Şifre: `admin`

### Django Admin Bilgileri
Süper kullanıcı oluşturmak için aşağıdaki komutu kullanabilirsiniz:
```bash
docker-compose exec web python manage.py createsuperuser
```

### Testleri Çalıştırma
Fonksiyonların doğruluğunu kontrol etmek için birim testlerini şu komutla çalıştırabilirsiniz:
```bash
docker-compose exec web python manage.py test
```
**Not**: Projeye 2 gün vakit ayırabildiğim için Frontend tarafı yarım kaldı, bilginize.