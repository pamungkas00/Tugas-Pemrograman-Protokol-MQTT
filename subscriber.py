import paho.mqtt.client as mqtt

# Callback saat subscriber berhasil terhubung ke broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Suksess terhubung ke Mosquitto Broker!")
        
        # =================================================================
        # SILAHKAN AKTIFKAN SALAH SATU SKENARIO DI BAWAH INI:
        # =================================================================
        
        # Skenario 1: Komunikasi Dasar (Satu topik spesifik)
        #client.subscribe("smart_agri/field1/sensor/temperature", qos=0)
        
        # Skenario 4: Penggunaan Wildcard + (Semua lahan, khusus sensor suhu)
        client.subscribe("smart_agri/+/sensor/temperature", qos=1)
        
        # Skenario 5: Penggunaan Wildcard # (Semua data di bawah root smart_agri)
        #client.subscribe("smart_agri/#", qos=2)
        
        print("Berhasil melakukan Subscribe.")
    else:
        print(f"Gagal terhubung, result code: {rc}")

# Callback saat ada pesan masuk
def on_message(client, userdata, msg):
    print(f"\n[PESAN MASUK]")
    print(f"Topik : {msg.topic}")
    print(f"QoS   : {msg.qos}")
    print(f"Data  : {msg.payload.decode('utf-8')}")

# Konfigurasi Broker
BROKER = "localhost"
PORT = 1883

# Inisialisasi Client
try:
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
    client = mqtt.Client()

# Menghubungkan fungsi callback
client.on_connect = on_connect
client.on_message = on_message

print("Subscriber Smart Agriculture menunggu data...")
client.connect(BROKER, PORT, 60)

# Loop selamanya untuk mendengarkan pesan
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber dihentikan.")
    client.disconnect()