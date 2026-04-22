import random
import time

class LoRaMeshSim:
    """
    LoRa Mesh Ağ Simülasyonu.
    Düşük güç, uzun mesafe ve düşük bant genişliği karakteristiklerini simüle eder.
    """
    def __init__(self, node_id, frequency="868MHz", tx_power=14):
        self.node_id = node_id
        self.frequency = frequency
        self.tx_power = tx_power
        self.neighbor_nodes = []

    def discover_neighbors(self):
        # Rastgele komşu keşfi simülasyonu
        potential_neighbors = ["DRO-01", "OP-02", "BASE-STATION", "RELAY-X"]
        self.neighbor_nodes = random.sample(potential_neighbors, k=random.randint(1, 3))
        print(f"[{self.node_id}] Komşular keşfedildi: {self.neighbor_nodes}")

    def send_data(self, target, payload):
        print(f"[{self.node_id}] '{target}' hedefine veri gönderiliyor (Frekans: {self.frequency})...")
        # Paket kaybı simülasyonu
        if random.random() > 0.95:
            print(f"!!! [{self.node_id}] PAKET KAYBI: '{target}' ulaşılamadı.")
            return False
        
        time.sleep(0.5) # İletim gecikmesi simülasyonu
        print(f"[{self.node_id}] İleti başarıyla gönderildi: {payload}")
        return True

if __name__ == "__main__":
    node = LoRaMeshSim(node_id="OP-01")
    node.discover_neighbors()
    node.send_data("BASE-STATION", "DURUM: BOLGE_TEMIZ")
