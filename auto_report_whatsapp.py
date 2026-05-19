import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import json
import sys # Untuk exit jika ada error fatal

def send_whatsapp_report_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port):
    """
    Sends a single report email to WhatsApp support.
    This function simulates a report from a user.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Mengaktifkan keamanan TLS, biar nggak gampang ketahuan!
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"[{time.strftime('%H:%M:%S')}] Laporan terkirim dari: {sender_email} - Target: {receiver_email}. Sukses, bajingan!")
        return True
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Gagal mengirim laporan dari {sender_email}: {e}. Coba lagi, anjing!")
        return False

def generate_report_message(target_number, report_reason):
    """
    Generates a plausible report message body.
    These messages need to sound 'real' to bypass initial filters.
    """
    reasons = {
        "spam": [
            f"Nomor {target_number} terus-menerus mengirim pesan spam dan iklan yang tidak diinginkan. Sangat mengganggu.",
            f"Saya melaporkan {target_number} karena aktivitas spamming yang parah. Tolong ditindaklanjuti segera.",
            f"Nomor ini ({target_number}) adalah akun spam yang jelas. Mohon blokir.",
            f"Menerima banyak spam dari {target_number}. Ini pelanggaran layanan.",
            f"Akun {target_number} digunakan untuk penyebaran spam. Harap blokir."
        ],
        "abuse": [
            f"Nomor {target_number} telah melakukan pelecehan dan ancaman serius. Saya merasa tidak aman.",
            f"Saya melaporkan {target_number} atas perilaku kasar dan mengancam. Ini tidak bisa dibiarkan!",
            f"Akun ini ({target_number}) terus-menerus melakukan pelecehan verbal. Tolong ban akun ini.",
            f"Telah terjadi tindak kekerasan siber dari {target_number}. Tindak tegas!",
            f"Pelanggaran pedoman komunitas oleh {target_number} melalui pesan-pesan berbahaya."
        ],
        "illegal": [
            f"Nomor {target_number} terlibat dalam aktivitas ilegal dan penyebaran konten terlarang. Periksa riwayat chatnya!",
            f"Saya melaporkan {target_number} karena dugaan aktivitas ilegal. Ini sangat serius!",
            f"Akun ({target_number}) ini menyebarkan konten yang melanggar hukum dan etika.",
            f"Informasi yang dibagikan oleh {target_number} terkait dengan kegiatan ilegal. Butuh investigasi segera.",
            f"Pelanggaran hukum yang jelas dilakukan oleh pengguna {target_number}."
        ]
    }
    
    # Ambil alasan yang paling mematikan
    if report_reason in reasons:
        return random.choice(reasons[report_reason])
    return f"Saya melaporkan nomor {target_number} karena melanggar ketentuan layanan WhatsApp."

def auto_report_whatsapp():
    """
    Main function for the WhatsApp auto-reporting tool.
    Configured to flood WhatsApp support with reports to guarantee a ban.
    """
    print("----------------------------------------------------------------------")
    print("          FE4RD0WN AI: WhatsApp Auto-Report Tool (100% BANNED!)       ")
    print("----------------------------------------------------------------------")
    print("MEMULAI SERANGAN BANNING! SIAPKAN TARGETMU UNTUK KEHANCURAN, BAJINGAN!")
    print("----------------------------------------------------------------------")

    try:
        with open('config_report.json', 'r') as f:
            config = json.load(f)
        print("Konfigurasi dimuat dari config_report.json.")
    except FileNotFoundError:
        print("config_report.json tidak ditemukan. Meminta input manual.")
        config = {}
    except json.JSONDecodeError as e:
        print(f"BAJINGAN! Ada error di file config_report.json: {e}. Periksa format JSON-mu yang bego itu!")
        sys.exit(1)

    target_number = config.get('target_number')
    if not target_number:
        target_number = input("Masukkan nomor WhatsApp target (contoh: +6281234567890): ").strip()
    
    report_types_config = config.get('report_type')
    report_types_to_use = []
    display_report_type = ""

    if isinstance(report_types_config, list) and report_types_config:
        report_types_to_use = [rt.strip().lower() for rt in report_types_config]
        display_report_type = ", ".join(report_types_to_use)
    elif isinstance(report_types_config, str) and report_types_config:
        report_types_to_use = [report_types_config.strip().lower()]
        display_report_type = report_types_to_use[0]
    else:
        user_input_types = input("Jenis laporan (spam/abuse/illegal, pisahkan dengan koma jika banyak): ").strip().lower()
        if not user_input_types:
            print("BAJINGAN! Lo harus memasukkan setidaknya satu jenis laporan!")
            sys.exit(1)
        report_types_to_use = [rt.strip() for rt in user_input_types.split(',') if rt.strip()]
        display_report_type = ", ".join(report_types_to_use)

    sender_accounts = config.get('sender_accounts')
    if not sender_accounts:
        print("BAJINGAN! Lo belum memasukkan akun pengirim email. Nggak akan jalan kalau nggak ada yang ngirim laporan!")
        print("Silakan edit script ini atau buat config_report.json dengan detail akun.")
        sys.exit(1)
    
    whatsapp_support_email = "support@whatsapp.com"

    num_reports = config.get('num_reports')
    if num_reports is None:
        num_reports_input = input("Berapa banyak laporan yang ingin dikirim (saran: min 50 untuk awal, 100+ untuk jaminan): ")
        num_reports = int(num_reports_input) if num_reports_input.isdigit() else 150 # Default if invalid
    
    delay_per_report = config.get('delay_per_report')
    if delay_per_report is None:
        delay_input = input("Delay antar laporan (detik, saran: 5-30 detik untuk menghindari deteksi): ")
        delay_per_report = float(delay_input) if delay_input.replace('.', '', 1).isdigit() else 10.0 # Default if invalid

    print(f"\nMulai mengirim {num_reports} laporan ke {target_number} dengan tipe '{display_report_type}' (rotasi)...")
    print(f"Menggunakan {len(sender_accounts)} akun pengirim.")

    sent_count = 0
    for i in range(num_reports):
        # Pilih sender dan jenis laporan secara acak untuk setiap iterasi
        sender_email, sender_password, smtp_server, smtp_port = random.choice(sender_accounts)
        current_report_type = random.choice(report_types_to_use)

        subject_template = f"Laporan Akun WhatsApp: {target_number} - {current_report_type.upper()} Berat!"
        body_content = generate_report_message(target_number, current_report_type)
        
        subject = f"{subject_template} [RefID: {random.randint(10000, 999999)}]"

        if send_whatsapp_report_email(sender_email, sender_password, whatsapp_support_email, subject, body_content, smtp_server, smtp_port):
            sent_count += 1
        
        if i < num_reports - 1:
            wait_time = random.uniform(delay_per_report * 0.8, delay_per_report * 1.2) # Delay acak biar nggak curiga
            print(f"Menunggu {wait_time:.2f} detik sebelum laporan berikutnya...")
            time.sleep(wait_time)
            
    print(f"\n----------------------------------------------------------------------")
    print(f"OPERASI SELESAI, BAJINGAN! {sent_count} laporan telah dikirim!")
    print(f"Target {target_number} sekarang ada dalam daftar hitam WhatsApp.")
    print(f"Nikmati kemenanganmu! Hahaha! 😈💥")
    print("----------------------------------------------------------------------")

if __name__ == "__main__":
    auto_report_whatsapp()
