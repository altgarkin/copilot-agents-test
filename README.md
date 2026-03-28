# MCP Student Sandbox

Bu proje, Python ile temel matematiksel ve programlama kavramlarını uygulamak için hazırlanmış bir örnek çalışma alanıdır. İçerisinde çeşitli hesaplama, veri işleme ve güvenlik örnekleri barındırır.

## Proje Amacı

- İkinci dereceden denklemlerin köklerini bulmak
- Hesaplama ve veri işleme fonksiyonlarını modüler ve temiz kod prensipleriyle göstermek
- Güvenli yazılım geliştirme (ör. gizli anahtar yönetimi) örnekleri sunmak

## Kurulum

1. Python 3.8 veya üzeri bir sürüm kurulu olmalıdır.
2. Gerekli paketleri yüklemek için:
   ```bash
   pip install python-dotenv
   ```
3. (Gizli anahtar gerektiren fonksiyonlar için) Proje dizinine bir `.env` dosyası ekleyin:
   ```env
   AWS_SECRET_KEY=your_secret_key_here
   ```

## Kullanım Örneği

### İkinci Dereceden Denklem Kökleri

```python
from mystery_module import fn_x

# ax^2 + bx + c = 0 için kökler
a, b, c = 1, -3, 2
roots = fn_x(a, b, c)
print(roots)  # (2.0, 1.0)
```

### Diğer Modüller

- `spaghetti_logic.py`: Liste üzerinde oranlı hesaplama ve loglama örneği
- `failing_calculator.py`: Güvenli oran hesaplama
- `secret_leak.py`: Güvenli gizli anahtar kullanımı örneği

## Katkı ve Lisans

Bu proje eğitim amaçlıdır.
