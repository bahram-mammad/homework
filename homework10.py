# 1)
# import time

# for i in range(5, -1, -1):
#     print(f'{i} saniye')
#     time.sleep(1)

# print('bitdi')


# -------------------------------------------


# 3) 

# users = [
    
#     {"device": "iphone", "price": 3000, "count": null}, 
#     {"device": "samsung", "price": 2500, "count": 3},
#     {"device": "xiaomi", "price": 2100, "count": null},
#     {"device": "nokia", "price": 1800, "count": 4}

# ]


# import json

# json_data = '[{"device": "iphone", "price": 3000, "count": null}, {"device": "samsung", "price": 2500, "count": 3}, {"device": "xiaomi", "price": 2100, "count": null}, {"device": "nokia", "price": 1800, "count": 4}]'

# data = json.loads(json_data)
# print(data)

# users=[
    
#     {'device': 'iphone', 'price': 3000, 'count': None}, 
#     {'device': 'samsung', 'price': 2500, 'count': 3}, 
#     {'device': 'xiaomi', 'price': 2100, 'count': None}, 
#     {'device': 'nokia', 'price': 1800, 'count': 4}

# ]


# -----------------------------------------------


# 2)
# Oldugunuz dirde dersler deye bir folder yaradin. Sonra hemin foldere ders1.txt ve ders2.txt elave edin.
# Daha sonra ders1.txt silin ve ders2.txt adini deyisib, Python Notlar yazin. 
# Sonra ic-ice Python/General Python deye folderler hazirlayin. Ardindan Python Notlar faylini ora elave edin. 
# Daha sonra eyni faylin kopyasini Desktopa atin. En sonda da dersler folderini silin.



# import os
# import shutil

# os.mkdir('dersler')
# open(r'dersler/ders1.txt', 'a') 
# open(r'dersler/ders2.txt', 'a')
# os.remove(r'dersler/ders1.txt')
# os.replace(f'dersler/ders2.txt', f'dersler/Python Notlar')
# os.makedirs('./Python/General Python')
# shutil.move(r'dersler/Python Notlar', './Python/General Python')
# shutil.copyfile('./Python/General Python/Python Notlar', 'C:/Users/Baxram/OneDrive/Desktop/Python Notlar')
# shutil.rmtree('dersler')
