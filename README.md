# Smart Agriculture Monitoring System (MQTT)

Proyek ini adalah implementasi sistem pemantauan pertanian cerdas (*Smart Agriculture*) berbasis IoT menggunakan protokol **MQTT**. Sistem ini mensimulasikan pengiriman data dari tiga sensor kritikal: **Suhu Udara**, **Kelembapan Udara**, dan **Kelembapan Tanah (*Soil Moisture*)**.

Proyek ini dibuat untuk memenuhi tugas mata kuliah Pemrograman Protokol Komunikasi IoT dengan memenuhi 5 skenario pengujian MQTT (Dasar, QoS Berbeda, Multi-Topik, Wildcard `+`, dan Wildcard `#`).

---

## 🛠️ Spesifikasi Teknis
* **MQTT Broker:** Mosquitto Broker (`localhost:1883`)
* **Bahasa Pemrograman:** Python 3.12+
* **Library MQTT:** `paho-mqtt` (Kompatibel dengan API v2.x)
* **Protokol:** MQTT v3.1.1 / v5.0

---

## 📂 Struktur Topik MQTT
* `smart_agri/field1/sensor/temperature` (QoS 0)
* `smart_agri/field1/sensor/humidity` (QoS 1)
* `smart_agri/field1/sensor/soil` (QoS 2)

---

## 🚀 Panduan Instalasi dan Persiapan

### 1. Prasyarat
Pastikan Anda sudah menginstal **Mosquitto Broker** di komputer Anda. 
* Di Windows, pastikan layanan `Mosquitto Broker` sudah dalam status **Running** melalui *Services.msc* atau jalankan perintah berikut di CMD (Admin):
  ```bash
  net start mosquitto

### 2. Instalasi Library Python
Buka terminal pada direktori proyek ini, aktifkan virtual environment Anda (jika ada), lalu instal dependensi library yang dibutuhkan:
  `
  net start mosquitto
  `

## 💻 Cara Menjalankan Program
Untuk melakukan pengujian, Anda disarankan membuka dua jendela terminal terpisah di komputer Anda.

### Langkah 1: Jalankan Subscriber (Penerima Data)
Di Terminal 1, jalankan skrip subscriber untuk mulai mendengarkan data dari broker:
  ``bash
  python subscriber.py


### Langkah 2: Jalankan Publisher (Pengirim Data/Sensor Node)
Di Terminal 2, jalankan skrip publisher untuk mulai mensimulasikan dan mengirim data sensor secara berkala (setiap 5 detik):
    ``bash
    python publisher.py


## 🧪 Panduan Pengujian 5 Skenario
Skrip publisher.py secara default mengirimkan semua jenis data dengan tingkat QoS yang berbeda secara otomatis. Untuk menguji skenario tertentu di sisi Subscriber, buka file subscriber.py, cari fungsi on_connect(), lalu sesuaikan tanda komentar (#) pada baris subscribe seperti panduan di bawah ini:

### Skenario 1: Komunikasi Dasar Publisher–Subscriber
Tujuan: Membuktikan koneksi dasar 1-ke-1 pada topik spesifik.

Konfigurasi subscriber.py:
    ``bash
    client.subscribe("smart_agri/field1/sensor/temperature", qos=0)

Hasil: Subscriber hanya akan menerima data dari sensor suhu saja

### Skenario 2 & 3: QoS Berbeda & Penggunaan Beberapa Topik
Tujuan: Membuktikan pengiriman data ke jalur terpisah dengan keandalan berbeda (Suhu = QoS 0, Kelembapan Udara = QoS 1, Kelembapan Tanah = QoS 2).

Konfigurasi subscriber.py:
    ``bash
    client.subscribe("smart_agri/#", qos=2)

Hasil: Perhatikan log terminal subscriber, baris QoS : X dan Topik : ... akan berubah secara dinamis sesuai karakteristik masing-masing sensor.

### Skenario 4: Penggunaan Wildcard + (Single-Level)
Tujuan: Menyaring data satu level hirarki (contoh: mengambil data suhu dari lahan (field) mana saja).

Konfigurasi subscriber.py:
    ``bash
    client.subscribe("smart_agri/+/sensor/temperature", qos=1)

Hasil: Subscriber mengabaikan data kelembapan udara dan tanah, namun siap menerima data suhu dari field1, field2, dst.


### Skenario 5: Penggunaan Wildcard # (Multi-Level)
Tujuan: Menerima seluruh data sensor secara massal di bawah bendera topik utama.

Konfigurasi subscriber.py:
    ``bash
    client.subscribe("smart_agri/#", qos=2)

Hasil: Seluruh payload JSON dari semua sensor akan tertangkap secara berurutan dan simultan.