# Adrian Aryaputra Hamzah - 2206811474
# Event-Driven with Kafka


## Overview Aplikasi

### Struktur Aplikasi
```
.
├── README.md
├── constant.py
├── consumer_payment.py
├── consumer_ticket.py
├── docker-compose.yml
├── producer.py
├── requirement.txt
└── serealize_deserialize.py
```

### Arsitektur Aplikasi
```
producer.py ---> Kafka (topic: "flight-booking") ---> consumer_payment.py (group_id: "payment-group")
                                                 ---> consumer_ticket.py (group_id: "ticket-group")
```
Penjelasan:
1. `producer.py` akan mengirimkan 5 event (berupa data booking pesawat) ke Kafka melalui topic `flight-booking`
2. `consumer_payment.py` secara aktif mengonsumsi topik `flight-booking` dari Kafka pada group id `payment-group`. Ketika tahap (1) selesai dilaksanakan, maka event yang dikirimkan `producer.py` akan dikonsumsi oleh `consumer_payment.py`
3. `consumer_ticket.py` secara aktif mengonsumsi topik `flight-booking` dari Kafka pada group id `ticket-group`. Ketika tahap (1) selesai dilaksanakan, maka event yang dikirimkan `producer.py` akan dikonsumsi oleh `consumer_ticket.py`

## Getting Started

### 1. Setup Environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Inisialisasi Kafka dengan Docker
```
docker compose up -d
```

### Note: Jika ingin reset queue dengan docker
```
docker compose down
docker compose up -d
```

## Simulasi Event-driven dengan Kafka

### 1. Siapkan 3 sesi terminal

### 2. [Session 1] Jalankan consumer payment
```
python3 consumer_payment.py
```

### 3. [Session 2] Jalankan consumer ticket
```
python3 consumer_ticket.py
```

### 4. [Session 3] Jalankan producer
```
python3 producer.py
```

### 5. [Session 1 & 2] Perhatikan consumer payment dan ticket
Setiap 5 detik, akan muncul event yang dikirimkan oleh `producer.py`

### 6. [DEMO OFFSET: Session 1] Hentikan consumer payment
Setelah semua event (5 event) berhasil dikirimkan `producer.py`, hentikan consumer payment (Ctrl + C atau Cmd + C)

### 7. [Session 3] Jalankan producer kembali
```
python3 producer.py
```

### 8. [DEMO OFFSET: Session 1] Jalankan consumer payment kembali
```
python3 consumer_payment.py
```

### 8. [DEMO OFFSET: Session 1] Perhatikan consumer payment
Perhatikan bahwa `consumer_payment.py` hanya membaca event/message yang baru dari langkah 7. Hal ini disebabkan oleh offset.


## Highlights

### Consumer bersifat Independen
Meskipun kedua consumer membaca topic yang sama: `flight-booking`, pembacaan/konsumsi event dari masing masing consumer, tidak akan mengganggu alur konsumsi event dari consumer lainnya. Hal ini disebabkan karena mereka menggunakan [group id yang unik](#arsitektur-aplikasi). Setiap group id memiliki offset masing masing

### Offset
Kafka mencatat posisi (offset) terakhir dari pesan yang telah dibaca dari setiap consumer group. Ketika consumer dihentikan lalu dijalankan kembali, maka consumer hanya akan membaca pesan dari offset terakhir yang dicatat, bukan dari awal.

## Penjelasan

### Bagaimana komunikasi asynchronous bekerja?
Komunikasi asynchronous bekerja dengan mengirimkan event ke Kafka tanpa menunggu balasan dari consumer. Setelah seluruh event berhasil dikirimkan, maka producer langsung selesai.

### Apa perbedannya dengan komunikasi request-response?
Pada konteks request-response, pihak yang mengirimkan request harus menunggu hingga pihak yang menerima request menyelesaikan pemrosesan request, lalu mengembalikan response. Hal ini dapat menjadi masalah ketika pihak penerima sedang tidak dapat diakses, atau membutuhkan waktu yang sangat lama untuk dapat diproses.

### Disclosure
Saya menggunnakan Generative AI (claude) untuk kode pada tahap awal. Setelahnya, saya melakukan modifikasi sesuai requirement.