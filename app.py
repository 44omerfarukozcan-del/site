from flask import Flask, render_template, request

app = Flask(__name__)

# --- 30 ADET PROJE VE İLGİ ALANI VERİSİ ---
projeler_verisi = [
    {'id': 1, 'baslik': '❤️ Nehir & Samet Web Sitesi', 'ozet': 'Samet ve Nehir için tasarlanan özel Sevgililer Günü sitesi.', 'ikon': 'fas fa-heart', 'renk': '#e94560'},
    {'id': 2, 'baslik': '📱 iPhone 7 Teardown Art', 'ozet': 'Eski iPhone 7 cihazını parçalarına ayırıp çerçeveleme sanatı.', 'ikon': 'fas fa-tools', 'renk': '#f1c40f'},
    {'id': 3, 'baslik': '🎓 DGS 2027 Yol Haritası', 'ozet': 'Bilgisayar Mühendisliği geçiş süreci için çalışma planlayıcı.', 'ikon': 'fas fa-graduation-cap', 'renk': '#3498db'},
    {'id': 4, 'baslik': '🦅 Beşiktaş Taraftar Portalı', 'ozet': 'Siyah-Beyaz sevdayı dijitale taşıyan fan sayfası tasarımı.', 'ikon': 'fas fa-eagle', 'renk': '#ffffff'},
    {'id': 5, 'baslik': '💻 Excalibur G915 Benchmark', 'ozet': 'Casper Excalibur G915 laptop performans optimizasyon raporu.', 'ikon': 'fas fa-laptop-code', 'renk': '#2ecc71'},
    {'id': 6, 'baslik': '🌊 Samsun Yerel Rehber', 'ozet': 'Samsun\'daki teknoloji noktaları ve öğrenci rehberi.', 'ikon': 'fas fa-map-marked-alt', 'renk': '#e67e22'},
    {'id': 7, 'baslik': '🐍 Python Backend API', 'ozet': 'Flask kullanılarak geliştirilmiş güvenli bir RESTful API.', 'ikon': 'fab fa-python', 'renk': '#9b59b6'},
    {'id': 8, 'baslik': '🗄️ SQL Veritabanı Tasarımı', 'ozet': 'Öğrenci yönetim sistemi için normalize edilmiş SQL mimarisi.', 'ikon': 'fas fa-database', 'renk': '#1abc9c'},
    {'id': 9, 'baslik': '📝 Markdown Not Tutucu', 'ozet': 'Ders notlarını hızlıca dijitale aktaran web arayüzü.', 'ikon': 'fas fa-file-alt', 'renk': '#34495e'},
    {'id': 10, 'baslik': '📉 DGS Deneme Takipçisi', 'ozet': 'Matematik ve Sayısal Mantık netlerini grafiklerle takip etme.', 'ikon': 'fas fa-chart-line', 'renk': '#e74c3c'},
    {'id': 11, 'baslik': '⚡ Flask Portfolio v1', 'ozet': 'İlk kişisel portfolyo sitemin geliştirme süreci.', 'ikon': 'fas fa-briefcase', 'renk': '#16a085'},
    {'id': 12, 'baslik': '🛠️ Donanım İnceleme Bloğu', 'ozet': 'G915 ve çevre birimleri üzerine donanım inceleme serisi.', 'ikon': 'fas fa-microchip', 'renk': '#d35400'},
    {'id': 13, 'baslik': '📂 GitHub Workflow', 'ozet': 'Kodlarımı düzenli tutmak için kullandığım Git akışları.', 'ikon': 'fab fa-github', 'renk': '#7f8c8d'},
    {'id': 14, 'baslik': '⏰ Pomodoro Çalışma Aracı', 'ozet': 'DGS derslerine odaklanmak için geliştirilen zamanlayıcı.', 'ikon': 'fas fa-hourglass-half', 'renk': '#c0392b'},
    {'id': 15, 'baslik': '🖼️ Frame Design Tool', 'ozet': 'iPhone teardown taslaklarını dijitalde önizleme aracı.', 'ikon': 'fas fa-palette', 'renk': '#8e44ad'},
    {'id': 16, 'baslik': '🔒 Şifre Yöneticisi', 'ozet': 'Python ile geliştirilmiş yerel şifre saklama yazılımı.', 'ikon': 'fas fa-lock', 'renk': '#2c3e50'},
    {'id': 17, 'baslik': '☁️ Bulut Sunucu Kurulumu', 'ozet': 'Sitemi yayına almak için Linux sunucu konfigürasyonu.', 'ikon': 'fas fa-server', 'renk': '#2980b9'},
    {'id': 18, 'baslik': '📱 Mobil Uyumlu Tasarım', 'ozet': 'Tüm cihazlarda çalışan responsive CSS kütüphanesi.', 'ikon': 'fas fa-mobile-screen', 'renk': '#27ae60'},
    {'id': 19, 'baslik': '🤖 Chatbot Denemeleri', 'ozet': 'Kullanıcı sorularını yanıtlayan basit bir Python botu.', 'ikon': 'fas fa-robot', 'renk': '#f39c12'},
    {'id': 20, 'baslik': '📅 Haftalık Ders Programı', 'ozet': 'Üniversite derslerini ve DGS kamplarını organize eden takvim.', 'ikon': 'fas fa-calendar-alt', 'renk': '#bdc3c7'},
    {'id': 21, 'baslik': '🎮 Python Oyun: Snake', 'ozet': 'Klasik yılan oyununun Python ile kodlanmış versiyonu.', 'ikon': 'fas fa-gamepad', 'renk': '#16a085'},
    {'id': 22, 'baslik': '🏗️ Mimari Yapı Analizi', 'ozet': 'Backend projelerimde kullandığım MVC mimarisi.', 'ikon': 'fas fa-sitemap', 'renk': '#2c3e50'},
    {'id': 23, 'baslik': '🔍 SEO Optimizasyonu', 'ozet': 'Sitemin Google aramalarında üst sıralara çıkma çalışmaları.', 'ikon': 'fas fa-search', 'renk': '#e67e22'},
    {'id': 24, 'baslik': '🛒 E-Ticaret Arayüzü', 'ozet': 'Ürün listeleme ve sepet mantığı üzerine prototip.', 'ikon': 'fas fa-shopping-cart', 'renk': '#2980b9'},
    {'id': 25, 'baslik': '🎨 CSS Animasyon Kütüphanesi', 'ozet': 'Sitedeki geçiş efektleri için özel CSS kodları.', 'ikon': 'fas fa-wand-magic-sparkles', 'renk': '#9b59b6'},
    {'id': 26, 'baslik': '📧 Mail Otomasyonu', 'ozet': 'Form verilerini mail olarak gönderen Python scripti.', 'ikon': 'fas fa-envelope-open-text', 'renk': '#c0392b'},
    {'id': 27, 'baslik': '⚖️ Algoritma Karmaşıklığı', 'ozet': 'Big O notation üzerine yazdığım teknik makale.', 'ikon': 'fas fa-infinity', 'renk': '#7f8c8d'},
    {'id': 28, 'baslik': '🏁 Beşiktaş Maç Takibi', 'ozet': 'Kartal\'ın maçlarını anlık takip eden küçük bir araç.', 'ikon': 'fas fa-flag', 'renk': '#000000'},
    {'id': 29, 'baslik': '📐 Sayısal Mantık Notları', 'ozet': 'DGS sınavının en zor kısmı için çözümlü örnekler.', 'ikon': 'fas fa-square-root-variable', 'renk': '#d35400'},
    {'id': 30, 'baslik': '🚀 Gelecek Vizyonu 2027', 'ozet': 'Mühendislik mezuniyeti sonrası kariyer hedefleri.', 'ikon': 'fas fa-rocket', 'renk': '#27ae60'}
]

@app.route('/')
def anasayfa():
    return render_template('index.html', projeler=projeler_verisi)

@app.route('/dersler')
def dersler():
    # 100 Not Döngüsü
    ders_notlari = []
    for i in range(1, 101):
        ders_notlari.append({
            'konu': f'Yazılım Konusu #{i}',
            'detay': f'Bu {i}. ders notunda backend mimarisinin ve Python geliştirme süreçlerinin detaylarını öğreniyoruz.',
            'kod': f'print("Ders {i} tamamlandı")',
            'etiket': 'Python' if i % 2 == 0 else 'Flask'
        })
    return render_template('dersler.html', notlar=ders_notlari)

@app.route('/hakkimda')
def hakkimda():
    return render_template('hakkimda.html')

@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

if __name__ == '__main__':
    app.run(debug=True)