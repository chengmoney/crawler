import requests
url = "http://img0.dili360.com/pic/2020/01/06/5e13017656f248f08145799_t.jpg@!rw9"
r = requests.get(url)
# print(r.status_code)
with open('xx.jpg', 'wb') as f:
    f.write(r.content)
