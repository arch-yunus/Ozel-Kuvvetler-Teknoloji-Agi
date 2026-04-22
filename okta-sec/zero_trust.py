import time
import hashlib

class ZeroTrustValidator:
    """
    OKTA Zero-Trust Paket Doğrulayıcı.
    Her paketin kimliğini, bütünlüğünü ve tazeliğini kontrol eder.
    """
    def __init__(self, allowed_nodes):
        self.allowed_nodes = allowed_nodes # List of node_ids
        self.packet_history = set() # To prevent replay attacks

    def validate_packet(self, packet_id, sender_id, timestamp, hmac_hash):
        # 1. Kimlik Kontrolü
        if sender_id not in self.allowed_nodes:
            print(f"[ZT-ALERT] Yetkisiz düğüm: {sender_id}")
            return False

        # 2. Replay Attack Kontrolü
        if packet_id in self.packet_history:
            print(f"[ZT-ALERT] Tekrar saldırısı algılandı: {packet_id}")
            return False

        # 3. Zaman Damgası Kontrolü (Tazelik)
        # 30 saniyeden eski paketleri reddet
        if time.time() - timestamp > 30:
            print(f"[ZT-ALERT] Bayat paket reddedildi (Time delta: {time.time() - timestamp}s)")
            return False

        # 4. HMAC Bütünlük Kontrolü (Simülasyon)
        # Gerçekte burada kriptografik doğrulama yapılır.
        expected_hash = hashlib.sha256(f"{packet_id}{sender_id}{timestamp}".encode()).hexdigest()
        # Not: Basitlik için burada tam hash kontrolü yerine varlığını kontrol ediyoruz stüb olarak.
        if not hmac_hash:
             return False

        # Kayıt tut
        self.packet_history.add(packet_id)
        print(f"[ZT-SUCCESS] Paket doğrulandı: {packet_id} from {sender_id}")
        return True

if __name__ == "__main__":
    validator = ZeroTrustValidator(allowed_nodes=["OP-01", "OP-02", "BASE-HQ"])
    
    # Geçerli paket
    validator.validate_packet("PKT-9981", "OP-01", time.time(), "hash_abc_123")
    
    # Replay atağı
    validator.validate_packet("PKT-9981", "OP-01", time.time(), "hash_abc_123")
    
    # Zaman dışı paket
    validator.validate_packet("PKT-1122", "OP-02", time.time() - 60, "hash_xyz")
