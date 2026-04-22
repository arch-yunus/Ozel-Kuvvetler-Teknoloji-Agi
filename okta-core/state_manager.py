import json
import logging

class StateManager:
    """
    OKTA Durum Yöneticisi (CRDT Tabanlı Senkronizasyon Simülasyonu).
    Düğümler arası ortak durumsal farkındalık resmini tutarlı tutar.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        # Lokal durum: {object_id: {data}}
        self.situational_awareness = {
            "HQ": {"status": "ONLINE", "pos": (0,0)},
            "WEATHER": {"temp": 22, "wind": 5}
        }

    def update_object(self, object_id, data):
        """
        Lokal veriyi günceller ve senkronizasyon paketi oluşturur.
        """
        if object_id not in self.situational_awareness:
            self.situational_awareness[object_id] = {}
        
        self.situational_awareness[object_id].update(data)
        self.situational_awareness[object_id]["last_updated_by"] = self.node_id
        
        sync_packet = {
            "type": "STATE_SYNC",
            "obj_id": object_id,
            "data": data,
            "origin": self.node_id
        }
        print(f"[STATE] Lokal durum güncellendi. Senkronizasyon yayılıyor: {object_id}")
        return sync_packet

    def merge_remote_state(self, sync_packet):
        """
        Uzak düğümden gelen veriyi yerel duruma ekler (Conflict Resolution).
        """
        obj_id = sync_packet["obj_id"]
        remote_data = sync_packet["data"]
        
        if obj_id not in self.situational_awareness:
            self.situational_awareness[obj_id] = {}
        
        # Basit Last-Writer-Wins (LWW) yaklaşımı
        self.situational_awareness[obj_id].update(remote_data)
        self.situational_awareness[obj_id]["synced_from"] = sync_packet["origin"]
        print(f"[STATE] Düğüm {sync_packet['origin']}'den gelen veriler birleştirildi: {obj_id}")

if __name__ == "__main__":
    sm = StateManager(node_id="ALPHA-1")
    
    # Kendi durumunu güncelle
    p1 = sm.update_object("TEAM-B", {"pos": (12, 45), "hp": 100})
    
    # Başka düğümden veri gelmiş gibi yap
    remote_p = {"obj_id": "TEAM-C", "data": {"pos": (5, 9), "hp": 90}, "origin": "BETA-2"}
    sm.merge_remote_state(remote_p)
    
    print(f"Final Durumsal Resim: {json.dumps(sm.situational_awareness, indent=2)}")
