# OKTA Taktik Protokoller

Bu doküman, OKTA ağında kullanılan veri paketleme ve yönlendirme protokollerini detaylandırır.

## 1. Taktik Veri Paketi (TVP) Yapısı

OKTA ağındaki tüm iletişim, düşük bant genişliğine sahip (LoRa gibi) kanallar için optimize edilmiş **Taktik Veri Paketi (TVP)** formatını kullanır.

| Alan | Boyut (Byte) | Açıklama |
| :--- | :--- | :--- |
| **Header** | 4 | Protokol versiyonu ve paket tipi. |
| **Sender ID** | 8 | Gönderen düğümün benzersiz kimliği. |
| **Target ID** | 8 | Hedef düğüm (0x00 = Broadcast). |
| **Payload Size**| 2 | Veri yükünün boyutu. |
| **Payload** | Değişken | Şifrelenmiş taktik veri. |
| **HMAC/MAC** | 16 | Veri bütünlüğü ve kimlik doğrulama. |

## 2. OKTA-DFS (Dynamic Frequency Selection)

Sinyal kestirilmesini ve elektronik harp (EW) saldırılarını engellemek için OKTA, **Dinamik Frekans Seçimi** algoritmasını kullanır.

- **Frekans Atlamalı Spread Spectrum (FHSS)**: Saniyede 10 ila 100 kez frekans değişimi.
- **LPI (Low Probability of Intercept)**: Sinyal gücünün arka plan gürültüsü içinde gizlenmesi.

## 3. Yönlendirme Algoritması: Mesh-Route v2

OKTA, merkezi bir yönlendiriciye ihtiyaç duymadan en kısa ve güvenli yolu bulan **Mesh-Route v2** algoritmasını kullanır.

1. **Neighbor Discovery**: Düğümler periyodik olarak düşük güçte "HELLO" paketi yayınlar.
2. **Path Scoring**: Yol puanı; sinyal kalitesi (RSSI), düğüm batarya seviyesi ve trafik yoğunluğuna göre hesaplanır.
3. **Store-and-Forward**: Bağlantı koptuğunda veriler düğümde saklanır ve ilk fırsatta iletilir.

## 4. Öncelik Seviyeleri (QoS)

- **PR-0 (FLASH)**: Acil durum sinyalleri, saldırı ihbarları. (Gecikme < 100ms)
- **PR-1 (IMMEDIATE)**: Konum güncellemeleri, komutlar.
- **PR-2 (PRIORITY)**: Sensör verileri, raporlar.
- **PR-3 (ROUTINE)**: Teçhizat durumları, loglar.
