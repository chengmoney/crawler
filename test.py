from urllib import request
url = 'http://httpbin.org'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
rq = request.Request(url, headers=header)
response = request.urlopen(rq)
print(response.code)
print(response.read().decode('utf8'))
