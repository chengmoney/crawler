from urllib import request
from urllib import parse
from pprint import pprint
data = {'chengyu': '成驭'}
# 加入data参数后自动变为post请求

rsp = request.urlopen('http://httpbin.org/post', data=bytes(parse.urlencode(data), encoding='utf8'))
print(rsp.read().decode('utf-8'))
print(rsp.geturl())

# 创建一个HTTP get请求
response = request.urlopen('http://www.baidu.com')
# pprint(response.read().decode('utf-8'))

# 百度查询hello
# 构造查询url，通过network中发现查询为get请求，请求url为https://www.baidu.com/s

url = 'https://www.baidu.com/s?{}'
data = {'wd': 'hello'}
encode_data = parse.urlencode(data)
url_find = url.format(encode_data)
response1 = request.urlopen(url_find)
# pprint(response1.read().decode('utf8'))
# 这样不能查询出来，找不到页面。因为百度有反扒策略


# 尝试加上请求头
# 1.创建Request对象
# 2.创建Request对象时候加入自定义的header
# 3.header是以字典的形式，将user-agent修改为以下形式
# 4.request.urlopen()的参数可以为Response对象
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36'}
rq = request.Request(url_find, headers=header)
response2 = request.urlopen(rq)
# pprint(response2.read().decode('utf8'))
# 发现加了请求头之后还是不能找到页面

# 再将请求头中加入cookies试一试
# 加入cookies有两种方法
# 1.在在网站中network中找到头信息中的cookies
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36',
          'Cookie': 'BIDUPSID=66EBBC2BE42DADD77B7480566999C94E; PSTM=1574684382; BAIDUID=66EBBC2BE42DADD72079C1363F87E200:FG=1; BDUSS=AwdkNvWUdLSkx1TGpNdGZ6UWF6YUNiZ29CcC1nNDlrV3I3N3VuaH54a29Ha1ZmRVFBQUFBJCQAAAAAAAAAAAEAAABntKUnvMW-ssmtwdZiYWJ5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACiNHV8ojR1fTD; BD_UPN=12314753; BD_HOME=1; H_PS_PSSID=7548_32606_1467_32327_31254_32046_32115_31321_26350_32580; BDUSS_BFESS=AwdkNvWUdLSkx1TGpNdGZ6UWF6YUNiZ29CcC1nNDlrV3I3N3VuaH54a29Ha1ZmRVFBQUFBJCQAAAAAAAAAAAEAAABntKUnvMW-ssmtwdZiYWJ5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACiNHV8ojR1fTD; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=2; H_PS_645EC=42d40aXJrveVyRAbDzTKG3kVd0Ki7Ll7PkjftzgrhNYyJiY7K9ZZLSzObADXWluwAMT3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSVRTM=287'}
rq = request.Request(url_find, headers=header)
response3 = request.urlopen(rq)
# pprint(response3.read().decode('utf8'))


def save_html(response):
    content = response.read()
    with open('baidu.com.html', 'wb') as f:
        f.write(content)


# 保存网页
save_html(response3)
# ----------------------------------------------------------
# 2.