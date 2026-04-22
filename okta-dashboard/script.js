document.addEventListener('DOMContentLoaded', () => {
    const logView = document.querySelector('.log-view');
    const nodes = [
        { id: 'ALPHA-01', status: 'active', pos: { t: 40, l: 30 } },
        { id: 'BRAVO-02', status: 'active', pos: { t: 55, l: 60 } },
        { id: 'DELTA-05', status: 'warning', pos: { t: 20, l: 80 } },
        { id: 'HOSTILE-X', status: 'hostile', pos: { t: 70, l: 40 } }
    ];

    // Log ekleme fonksiyonu
    function addLog(message, type = '') {
        const p = document.createElement('p');
        if (type) p.className = type;
        const time = new Date().toLocaleTimeString();
        p.textContent = `> [${time}] ${message}`;
        logView.prepend(p);
        
        // Log sınırlama (son 15 log)
        if (logView.children.length > 15) {
            logView.removeChild(logView.lastChild);
        }
    }

    // Hedefleri haritada hareket ettir
    function updateMap() {
        const map = document.querySelector('.map-view');
        // Mevcut hedefleri temizle (Örnek amaçlı statik olanları bırakmıyoruz)
        document.querySelectorAll('.target').forEach(t => t.remove());

        nodes.forEach(node => {
            const el = document.createElement('div');
            el.className = `target ${node.status}`;
            
            // Hafif rastgele hareket simülasyonu
            const tOffset = (Math.random() - 0.5) * 2;
            const lOffset = (Math.random() - 0.5) * 2;
            
            el.style.top = `${node.pos.t + tOffset}%`;
            el.style.left = `${node.pos.l + lOffset}%`;
            el.setAttribute('title', node.id);
            map.appendChild(el);
        });
    }

    // Rastgele olay üretici
    function simulateEvents() {
        const events = [
            { msg: "MESH NODE ALPHA-01: SIGNAL STRENGTH 98%", type: 'active' },
            { msg: "ENCRYPTION KEYS ROTATED.", type: '' },
            { msg: "SENSOR DATA SYNCED: ALL NODES.", type: '' },
            { msg: "DELTA-05: BATTERY CRITICAL (12%).", type: 'warning' },
            { msg: "MOVEMENT DETECTED AT NORTH SECTOR.", type: 'hostile' }
        ];

        const randomEvent = events[Math.floor(Math.random() * events.length)];
        addLog(randomEvent.msg, randomEvent.type);
    }

    // Döngüleri başlat
    setInterval(updateMap, 2000);
    setInterval(simulateEvents, 4000);

    addLog("OKTA C2 INITIALIZED. SECURE LINK STABLISHED.");
});
