import requests
from bs4 import BeautifulSoup

# ショップ名：shop_name/評価：shop_eva/件数：shop_num/出品件数：shop_nol/開始日：shop_start/ブランド：shop_brand

load_url = "https://www.buyma.com/buyer/6020144.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# ショップ名 shop_name
buyer_name = soup.find(id="buyer_name")
for element10 in buyer_name.find_all("a"):
    t = element10.text
    shop_name = t
##    print(t)

# 評価 shop_eva
for element20 in soup.find_all(class_="buyer_eva_total_count"):
    t = element20.text
    shop_eva = t
##    print(t)


# 件数 shop_num
buyer_text = soup.find(id="left_rate")
for element30 in buyer_text.find_all(class_="buyer_eva_text", limit=2):
    t = element30.text
    shop_num = t.strip()
 ##   print(t.strip())

# 出品件数 shop_nol
selling = soup.find(class_="selling")
for element40 in selling.find_all("span"):
    t = element40.text +"件"
    shop_nol = t
 ##   print(t)

# 開始日 shop_start
profile = soup.find(class_="profile_txt")
for element50 in profile.select("dd", limit=1):
    t = element50.text
    shop_start = t.strip()
 ##   print(t.strip())

# 出品の多いブランド名 shop_brand
brand = soup.find(class_="profile_txt")
for element60 in brand.find_all("dd"):
    for element61 in element60.find_all(class_="path_arrow"):
        t = element61.text
        shop_brand = t.strip()
        print(t.strip())
        

print(shop_name + '\n\n' + shop_eva + '\n\n' + shop_num + '\n\n' + shop_nol + '\n\n' + shop_start + '\n\n' + shop_brand)

