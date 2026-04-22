import base64
import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class OKTAEncryption:
    """
    OKTA AES-256-GCM Şifreleme Sağlayıcısı.
    Taktik veri güvenliği için tasarlanmıştır.
    """
    def __init__(self, master_key: str):
        self.salt = b'\x12\xaf\x88\x9e\xcb\x22\x11\x55' # Örnek sabit salt (Gerçekte değişken olmalı)
        self.key = self._derive_key(master_key)

    def _derive_key(self, master_key: str):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        return kdf.derive(master_key.encode())

    def encrypt(self, data: str, associated_data: str = "OKTA-V1"):
        aesgcm = AESGCM(self.key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data.encode(), associated_data.encode())
        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    def decrypt(self, token: str, associated_data: str = "OKTA-V1"):
        try:
            aesgcm = AESGCM(self.key)
            raw_data = base64.b64decode(token)
            nonce = raw_data[:12]
            ciphertext = raw_data[12:]
            decrypted = aesgcm.decrypt(nonce, ciphertext, associated_data.encode())
            return decrypted.decode('utf-8')
        except Exception as e:
            print(f"[ERROR] Şifre çözme başarısız: {e}")
            return None

if __name__ == "__main__":
    # Test Kullanımı
    crypto = OKTAEncryption(master_key="OKTA_SECURE_SECRET_2026")
    msg = "HEDEF_TESPIT: SEKTOR_7"
    
    encrypted = crypto.encrypt(msg)
    print(f"Şifreli: {encrypted}")
    
    decrypted = crypto.decrypt(encrypted)
    print(f"Çözülen: {decrypted}")
