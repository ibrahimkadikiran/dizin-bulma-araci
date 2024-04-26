import os
import requests
import random
import string
import argparse
import pyfiglet
import urllib3

urllib3.disable_warnings()

def dizin_tara(url, dizinler):
    http_kodlar = {
        200: "OK",
        301: "Yönlendirildi",
        302: "Yönlendirildi",
        403: "Erişim Engellendi",
        404: "Bulunamadı",
        500: "Sunucu Hatası"
    }  
    bulunan_dizinler = []
    for dizin in dizinler:
        tam_url = f"{url}/{dizin}"
        response = requests.get(tam_url, verify=False)
        
        if response.status_code in http_kodlar:
            anlam = http_kodlar[response.status_code]
            bulunan_dizinler.append((tam_url, response.status_code, anlam))
            print(f"[++] Bulundu: {tam_url} ({response.status_code} - {anlam})")
    return bulunan_dizinler

def main():
    parser = argparse.ArgumentParser(description="DIZIN TARAMA ARACI")
    parser.add_argument("-u", "--url", help="Taranacak URL (https://example.com)", required=True)
    parser.add_argument("-w","--wordlist", help="Dizin listesi dosyasi")
    args = parser.parse_args()

    url = args.url

    dizinDosyasi = args.wordlist or "varsayilan_dizinler.txt"

    if not os.path.exists(dizinDosyasi):
        print("varsayilan dizin dosyasi bulunamadi. Lütfen programin dogru calismasi için bir dizin dosyasi olusturun.")
        return

    with open(dizinDosyasi, 'r') as dosya:
        dizinler = dosya.read().splitlines()

    bulunan_dizinler = dizin_tara(url, dizinler)

    dosya_adi = f"ciktilar{url.replace('/', '_')}.txt"
    with open(dosya_adi, "w") as cikti_dosyasi:
        for dizin, kod, anlam in bulunan_dizinler:
            cikti_dosyasi.write(f"{dizin} ({kod} - {anlam})\n")

    print(f"Sonuclar '{dosya_adi}' dosyasina kaydedildi.")

os.system("clear") 
ibrahim_figlet = pyfiglet.figlet_format("Dizin Tarama", font = "standard")

print(ibrahim_figlet+"versiyon 1.1")
print("İbrahim KADIKIRAN\nhttps://www.linkedin.com/in/ibrahimkadikiran\n")
if __name__ == "__main__":
    main()