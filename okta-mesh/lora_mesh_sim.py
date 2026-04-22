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

    def send_data(self, target, payload, hop_count=0):
        if hop_count > 5:
            print(f"!!! [{self.node_id}] HATA: TTL (Maksimum Sıçrama) aşıldı. Paket düşürüldü.")
            return False

        print(f"[{self.node_id}] {hop_count}. sıçrama: '{target}' hedefine veri yönlendiriliyor...")
        
        # Eğer hedef direkt komşuysa (Simülasyon)
        if target in self.neighbor_nodes:
            print(f"  -> [{self.node_id}] Hedef '{target}' direkt kapsama alanında. Veri iletildi.")
            return True
        
        # Değilse, rastgele bir komşu üzerinden zıpla
        if self.neighbor_nodes:
            next_hop = random.choice(self.neighbor_nodes)
            print(f"  -> [{self.node_id}] Hedef direkt görünmüyor. {next_hop} üzerinden zıplanıyor...")
            # Rekürsif sıçrama simülasyonu
            time.sleep(0.3)
            return self.send_data(target, payload, hop_count + 1)
        
        print(f"!!! [{self.node_id}] HATA: Yönlendirme yolu bulunamadı.")
        return False


if __name__ == "__main__":
    node = LoRaMeshSim(node_id="OP-01")
    node.discover_neighbors()
    node.send_data("BASE-STATION", "DURUM: BOLGE_TEMIZ")
