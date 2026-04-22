# OKTA Güvenlik Çerçevesi

OKTA ağı, "Asla Güvenme, Daima Doğrula" ilkesine dayanan **Zero-Trust (Sıfır Güven)** mimarisi üzerine inşa edilmiştir.

## 1. Zero-Trust İlkeleri

1. **Sürekli Doğrulama**: Her veri paketi, göndericinin kimliği ve bütünlüğü bazında doğrulanır.
2. **En Az Yetki (Least Privilege)**: Saha düğümleri sadece kendi görev sahaları için gerekli verilere erişebilir.
3. **Varsayılan Tehdit**: Ağın her zaman tehlikede olduğu ve düğümlerin ele geçirilebileceği varsayılır.

## 2. Kriptografik Mimari

### 2.1. Simetrik Şifreleme (Veri Aktarımı)
- **Algoritma**: AES-256-GCM (Authenticated Encryption with Associated Data).
- **Kullanım**: Taktik mesajlar, konum verileri ve sensör füzyonu.
- **Dönüşüm**: Anahtarlar 24 saatte bir veya her görev öncesi yenilenir.

### 2.2. Asimetrik Şifreleme (Anahtar Değişimi)
- **Algoritma**: RSA-4096 veya Elliptic Curve Cryptography (Ed25519).
- **Kullanım**: Yeni bir düğümün ağa katılması ve oturum anahtarlarının dağıtılması.

## 3. Anahtar Yönetimi ve Rotasyonu

- **D-Key (Dynamic Key)**: Her operasyonel düğüm, fiziksel olarak korunan bir donanım modülünde benzersiz bir anahtar taşır.
- **Self-Destruct**: Donanım müdahalesi (tampering) algılandığında veya uzaktan komutla kritik anahtarlar bellekten silinir (wipe).

## 4. Anti-Spoofing ve Replay Attack Koruması

1. **Paket Numaralandırma**: Tekrar edilen paketler (replay attack) sıra numarası kontrolü ile reddedilir.
2. **Zaman Damgası (Timestamp)**: Gönderim zamanı ile alım zamanı arasındaki fark belli bir eşiği aşarsa paket geçersiz sayılır.
3. **Fiziksel Doğrulama**: Düğümlerin coğrafi konumu ve sinyal karakteristiği, kimlik doğrulamanın bir parçası olarak kullanılır.
