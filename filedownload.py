import requests

img_data = requests.get('http://www.gunnerkrigg.com//comics/00000001.jpg').content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)