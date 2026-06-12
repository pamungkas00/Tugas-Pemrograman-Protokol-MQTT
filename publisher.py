import time
import json
import random
import paho.mqtt.client as mqtt

# Konfigurasi Broker
BROKER = "localhost"  # Ganti dengan IP Broker jika remote
PORT = 1883
KEEPALIVE = 60

# Inisialisasi Client Paho-MQTT (Kompatibel dengan v2.x)
try:
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
    client = mqtt.Client()  # Fallback untuk paho-mqtt versi lama

# Hubungkan ke Mosquitto Broker
print("Menghubungkan ke Mosquitto Broker...")
client.connect(BROKER, PORT, KEEPALIVE)

# Jalankan loop di background
client.loop_start()

print("Publisher Smart Agriculture aktif. Mengirim data setiap 5 detik...\n")

try:
    while True:
        # Simulasi Data Sensor
        val_temp = round(random.uniform(24.0, 34.0), 2)
        val_hum = round(random.uniform(60.0, 85.0), 2)
        val_soil = round(random.uniform(40.0, 70.0), 2)

        # Skenario 3: Definisi Beberapa Topik Berbeda
        topic_temp = "smart_agri/field1/sensor/temperature"
        topic_hum = "smart_agri/field1/sensor/humidity"
        topic_soil = "smart_agri/field1/sensor/soil"

        # Skenario 1 & 2: Pengiriman data dasar dengan QoS Berbeda
        # 1. Suhu dengan QoS 0
        payload_temp = json.dumps({"value": val_temp, "unit": "C"})
        client.publish(topic_temp, payload_temp, qos=0)
        print(f"[QoS 0] Terkirim -> {topic_temp} : {payload_temp}")

        # 2. Kelembapan Udara dengan QoS 1
        payload_hum = json.dumps({"value": val_hum, "unit": "%"})
        client.publish(topic_hum, payload_hum, qos=1)
        print(f"[QoS 1] Terkirim -> {topic_hum} : {payload_hum}")

        # 3. Kelembapan Tanah dengan QoS 2
        payload_soil = json.dumps({"value": val_soil, "unit": "%"})
        client.publish(topic_soil, payload_soil, qos=2)
        print(f"[QoS 2] Terkirim -> {topic_soil} : {payload_soil}")

        print("-" * 50)
        time.sleep(5)

except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.loop_stop()
    client.disconnect()