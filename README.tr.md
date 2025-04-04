# MacDNS

Mac DNS Ayarlarını Hızla Değiştirin  
🧪 macOS için Deneysel DNS Değiştirici

---

## Özellikler

- `networksetup` komutunu kullanarak sistem düzeyinde DNS sunucularını değiştirir  
- Mevcut ağ konumlarını listeler ve seçmenize olanak tanır  
- Sık kullanılan DNS sağlayıcıları arasında kolay geçiş yapılmasını sağlar  
- Otomatik DNS yapılandırmasına sıfırlama desteği  
- `zsh`, `bash` ve diğer POSIX uyumlu shell'lerle uyumlu  
- macOS 10.15+ (Catalina ve üzeri) ile test edilmiştir  

---

## Kurulum

1. Terminal'i açın  
2. Aşağıdaki komutları çalıştırın:

```bash
git clone https://github.com/makalin/MacDNS.git
cd MacDNS
chmod +x macdns
sudo cp macdns /usr/local/bin/
```

Alternatif olarak `/opt/homebrew/bin/` veya PATH'inizdeki başka bir dizine de kopyalayabilirsiniz.

---

## Kullanım

Terminal'de `macdns` komutunu çalıştırın:

```bash
macdns
```

Komut çalıştırıldığında:

1. Mevcut ağ konumlarını listeler  
2. Seçtiğiniz konum için mevcut DNS sunucularını gösterir  
3. Ön tanımlı DNS sağlayıcıları listesinden birini seçmenizi ister  
4. DNS ayarlarını uygular ve yeni DNS'yi onaylar

---

## Örnek DNS Sağlayıcıları

| Sağlayıcı     | Birincil DNS     | İkincil DNS     |
|---------------|------------------|------------------|
| Google        | 8.8.8.8          | 8.8.4.4          |
| Cloudflare    | 1.1.1.1          | 1.0.0.1          |
| OpenDNS       | 208.67.222.222   | 208.67.220.220   |
| Quad9         | 9.9.9.9          | 149.112.112.112  |
| AdGuard       | 94.140.14.14     | 94.140.15.15     |

---

## DNS Sıfırlama (Otomatik Moda Dön)

Eğer DNS ayarlarını otomatik moda döndürmek isterseniz şu komutu çalıştırın:

```bash
macdns reset
```

Bu işlem seçtiğiniz konum için DNS sunucularını sıfırlar ve macOS'un DHCP üzerinden DNS almasına izin verir.

---

## Bilinen Sorunlar

- `networksetup` komutu `sudo` gerektirir, bu nedenle betik `sudo` ile çalıştırılmalıdır.  
- Eğer DNS değişiklikleri hemen uygulanmazsa, ağı devre dışı bırakıp tekrar etkinleştirmek yardımcı olabilir.  
- macOS sistem bütünlüğü koruması (SIP) devredeyse bazı sistem dizinlerine kopyalama engellenebilir.

---

## Katkı Sağlama

Katkıda bulunmak ister misiniz? Harika!

1. Fork’layın 📌  
2. Bir branch oluşturun 🔧  
3. Değişikliklerinizi yapın 💻  
4. Pull Request gönderin 🚀

Tüm katkılar memnuniyetle karşılanır!

---

## Lisans

MIT Lisansı. Daha fazla bilgi için `LICENSE` dosyasına bakın.
