# Taktiksel İletişim Doktrinleri ve MANET Mimarisi

## Genel Bakış
Modern muharebe sahasında "Bilgi Üstünlüğü" (Information Superiority), ateş gücünden daha kritiktir. MANET (Mobile Ad Hoc Network), merkezi bir altyapıya ihtiyaç duymadan tim üyelerinin birbirlerini birer röle (relay) istasyonu olarak kullandığı dinamik bir ağ yapısıdır.

## Doktrinel Dönüşüm: Hiyerarşiden Ağ Yapısına

Geleneksel telsiz sistemlerinde bir liderin konuşması herkes tarafından dinlenir (Point-to-Multipoint). MANET ise timi bir "Veri Bulutu" haline getirir.

1. **Self-Healing (Kendi Kendini Onarma):** Doktrinel olarak, timin bir üyesi (örneğin sinyalci) devre dışı kalsa bile ağ çökmez. Diğer cihazlar en iyi yolu (path) saniyeler içinde otonom olarak bulur.
2. **Sessiz İletişim:** Sesli konuşma yerine veri (data) odaklı iletişim (sessiz el işaretlerinin dijital versiyonu). HUD üzerinden metin mesajı, hedef koordinatı veya video akışı paylaşımı.

## MANET Sistem Örnekleri ve Kullanım Alanları

- **L3Harris Falcon IV (AN/PRC-163):** Çift kanallı el telsizi. Bir kanalda standart ses, diğer kanalda MANET tabanlı veri akışı (ISR verileri).
- **Persistent Systems MPU5:** Yüksek bant genişliğine sahip MANET cihazı. Drone beslemelerini tüm tim üyelerine eş zamanlı olarak dağıtabilir.

---

## Taktiksel Senaryo: Meskun Mahal ve Şehir Çatışması (Urban Warfare)

- **Problem:** Beton ve çelik yapılar sinyalleri bloke eder. Binanın en üst katındaki operatör, bodrumdaki operatörle doğrudan görüşemez.
- **MANET Çözümü:** Ara katlardaki her operatör bir "düğüm" (node) görevi görür. Sinyal, kattan kata sıçrayarak (hopping) bodrumdan en üste kadar kesintisiz ulaşır.
- **Sonuç:** Meskun mahalde kör nokta kalmaz; timin tamamı tek bir organizma gibi hareket eder.

## Kısıtlar: Sinyal Disiplini ve Spektrum Yönetimi
MANET ağları, düşman ELINT (Electronic Intelligence) birimleri tarafından tespit edilebilir sinyaller yayar. Doktrinel olarak, sızma aşamasında "Emisyon Kontrolü" (EMCON) uygulanarak sistemlerin kapatılması veya düşük güç moduna alınması kritiktir.
