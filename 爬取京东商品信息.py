import requests
url = 'https://item.jd.com/100005092794.html'
kv = {'user-agent': 'mozilla/5.0'}
try:
    r = requests.get(url, headers=kv)
    # r = requests.get(url)
    r.raise_for_status
    print(r.text[:1000])
except:
    print('爬取失败')