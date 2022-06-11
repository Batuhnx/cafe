# Kategori ve ürünleri tutan liste
menu = {
    "1) İçecek": [
        ("Kola", 2.00),
        ("Fanta", 8.00),
        ("Çay", 2.00),
        ("Lipton", 5.00),
        ("Gazoz", 3.00),
        ("Kahve", 3.00)
    ],
    "2) Yemek": [
        ("Pizza", 10.00),
        ("Hamburger", 8.00),
        ("Sandviç", 6.00),
        ("Kuzu Güveç", 70.00),
        ("Sac Kavurma", 60.00)
    ],
    "3) Tatlı": [
        ("Dondurma", 5.00),
        ("Fıstıklı", 33.00),
        ("Mozaik", 30.00),
        ("Bella Vista", 20.00),
        ("Cheese Cake", 15.00),
        ("Tiramisu", 20.00),
        ("Macaron", 7.5)
    ],
    "0) siparişi tamamla": 1
}


# ana menüyü gösteren fonksiyon
def ana_menuyu_goster():
    # ekrana kategori yazdırır
    print("\nKategori:")

    # kategori listesini döngüye alıyoruz
    for category in menu:
        # kategori listesindeki her bir elemanı ekrana yazdırıyoruz
        print(category)

    # alt satıra geçiyoruz
    print("\n")


# kategori menüsünü gösteren fonksiyon
def menuyu_goster(category):
    x = 0
    # x değişkeni kategori listesindeki her bir elemanın index değerini tutar

    # kategori listesindeki her bir elemanı döngüye alıyoruz
    for item in menu[category]:
        print(f"{x}) {item[0]} - {item[1]}TL")

        # kategori listesindeki her bir elemanı ekrana yazdırıyoruz

        x += 1
        # x değişkenine 1 ekliyoruz


# ana fonksiyon
def main():
    siparis = []
    # sipariş listesini oluşturuyoruz

    # döngümüz sonsuza kadar devam edecek
    while True:
        ana_menuyu_goster()
        # ana menüyü gösteriyoruz

        # kullanıcıdan kategori seçmesini istiyoruz
        category = input("Seçim: ")
        if category == "":
            # eğer kullanıcı boş bir değer girdiyse

            continue
            # döngümüzü tekrar başlatıyoruz

        elif category == "1" or category == 1:
            # eğer kullanıcı 1 yazıp enter a basarsa

            category = "1) İçecek"
            # kategori değişkenine 1) içecek değerini atıyoruz

        elif category == "2" or category == 2:
            # eğer kullanıcı 2 yazıp entera basarsa

            category = "2) Yemek"
            # kategori değişkenine 2) Yemek değerini atıyoruz


        elif category == "3" or category == 3:
            # eğer kullanıcı 3 yazıp entera basarsa

            category = "3) Tatlı"
            # kategori değişkenine 3) Tatlı değerini atıyoruz

        elif category == 0 or category == "0":
            # eğer kullanıcı 0 yazıp entera basarsa

            break
            # döngümüzü bitiriyoruz

        menuyu_goster(category)
        # kategori menüsünü gösteriyoruz

        item = input("Seçim: ")
        # kullanıcıdan ürün seçmesini istiyoruz

        if item == "":
            # eğer kullanıcı boş bir değer girrerse

            break
            # döngümüzü bitiriyoruz

        print(
            f"Seçimin {menu[category][int(item)][0]} - {menu[category][int(item)][1]}TL")
        siparis.append(menu[category][int(item)])
        # seçilen ürünü sipariş listesine ekliyoruz ve ekrana yazdırıyoruz

        print("\n")
        # alt satıra geçiyoruz

    print("\nSiparişin:")
    # ekrana sipariş yazdırıyoruz

    for item in siparis:
        # sipariş listesindeki her bir elemanı döngüye alıyoruz

        print(f"{item[0]} - {item[1]}TL")
        # sipariş listesindeki her bir elemanı ekrana yazdırıyoruz

    print("Sipraiş toplamı:", sum([item[1] for item in siparis]), "TL")
    # sipariş listesindeki her bir elemanın tutarını topluyoruz


if __name__ == "__main__":
    # programın çalıştığında main fonksiyonunu çalıştırıyoruz

    main()
    # main fonksiyonunu çalıştırıyoruz
