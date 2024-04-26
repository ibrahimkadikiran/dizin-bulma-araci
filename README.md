# dizin-bulma-araci
Web sitelerindeki gizli ve önemli dizinleri otomatik olarak sizin verdiğiniz wordlist ile yada varsayalinda olan wordlist ile siteyi tarar ve size çıktıları kaydeder

Kullanmadan önce sisteminizde python veya python3 yüklü olduğuna emin olun.

Kullanımı ise 

python3 dizin.py -u https://example.com -w /home/kali/Desktop/dizinlistesi.txt

python3 dizin.py -u https://example.com 

python dizin.py -h

-u yada --url Taranacak Url adresin girilmesi zorunludur

-w yada --wordlist elinizde mevcut listesiyi sitede taratmak isterseniz yolunu belirtmeniz gerekiyor. Elinizde yoksa varsayilan olarak dizin listesini kullanacaktır. 
