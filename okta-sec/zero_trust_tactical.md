# Taktiksel Sıfır Güven (Tactical Zero-Trust) Mimarisi 

## Genel Bakış
Sıfır Güven doktrini, "Asla güvenme, her zaman doğrula" prensibi üzerine kuruludur. Geleneksel askeri ağlar çevre güvenliğine (perimeter) odaklanırken, taktiksel sıfır güven her cihazın, her operatörün ve her veri paketinin her an doğrulanmasını gerektirir.

## Uygulama Alanları ve Doktrinel Analiz

1. **Dinamik Kimlik Yönetimi:** Telsizler ve HUD sistemleri, biyometrik veriler veya kriptografik anahtarlar ile operatörün gerçekliğini sürekli denetler.
2. **"Esir Düştü" Protokolü:** Bir cihaz (düğüm) anormal hareketler gösterdiğinde veya timden bağımsız bir konuma gittiğinde, ağın geri kalanından otonom olarak izole edilir.
3. **Mikro-Segmentasyon:** Operasyon emri (OPORD) gibi kritik veriler, sadece yetkili rütbeye sahip cihazların görebileceği şekilde şifrelenir; ağın geneline sızılsa dahi bu veriye ulaşılamaz.

---

## Veri Güvenliği ve Kuantum Sonrası Kriptografi (PQC)

Gelecekte, kuantum bilgisayarların mevcut şifleme standartlarını (RSA/AES) kırması bir risktir. Araştırmalar, taktik ağların şimdiden kuantum-dirençli algoritmalara (Lattice-based cryptography vb.) geçiş yapması gerektiğini vurgular.

## Karşılaştırma: Endüstriyel Sıfır Güven vs Taktik Sıfır Güven
- **Endüstriyel:** Kesintisiz yüksek hızlı internet bağlantısı varsayar.
- **Taktik:** Düşük bant genişliği (Low Bandwidth) ve sık kesilen bağlantılar (Disconnected, Intermittent, Limited - DIL) altında çalışmak zorundadır.
- **Çözüm:** Hafifletilmiş kimlik doğrulama paketleri (Lightweight authentication).

## Sonuç
Sıfır Güven, bir yazılım katmanından ziyade bir askeri disiplindir. Dijital sahanın güvenliği, en zayıf halkanın (operatörün cihazı) güvenliği kadardır.
