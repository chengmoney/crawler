import requests
r = requests.get('http://www.baidu.com')
temp = r.status_code
print(temp)
content = r.text
print(content)
print(r.encoding)  # 从http头中猜测的编码  如果header中不存在charset,则认为编码为iso-8859-1
print(r.apparent_encoding)

