from urllib import request
from urllib import parse
from pprint import pprint
data = {'chengyu': '成驭'}
rsp = request.urlopen('http://httpbin.org/post', data=bytes(parse.urlencode(data), encoding='utf8'))
print(rsp.read().decode('utf-8'))
print(rsp.geturl())

# 创建一个HTTP get请求
response = request.urlopen('http://www.baidu.com')
# pprint(response.read().decode('utf-8'))

# 百度查询hello
url = 'http://www.baidu.com/'
data = {'wd': 'hello'}
encode_data = parse.urlencode(data).encode('utf8')
response1 = request.urlopen(url, encode_data)
# pprint(response1.read().decode('utf8'))
# 这样不能查询出来，找不到页面。因为百度有反扒策略

# 尝试加上请求头
# 1.创建Request对象
# 2.创建Request对象时候加入自定义的header
# 3.header是以字典的形式，将user-agent修改为以下形式
# 4.request.urlopen()的参数可以为Response对象
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36'}
rq = request.Request(url, encode_data, header)
response2 = request.urlopen(rq)
# pprint(response2.read().decode('utf8'))
# 发现加了请求头之后还是不能找到页面

# 再将请求头中加入cookies试一试
# 加入cookies有两种方法
# 1.在在网站中network中找到头信息中的cookies
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36',
          'Cookie': 'BAIDUID=1F52E0417470AFEA0A8FC7BD8190B8CA:FG=1; ' \
                    'BIDUPSID=1F52E0417470AFEA0A8FC7BD8190B8CA; PSTM=1574820638;' \
                    ' BD_UPN=12314353; H_WISE_SIDS=139914_141961_143438_142019_144884_141748_143' \
                    '161_144420_144134_141898_144483_136862_131246_144682_141261_144742_138883_1' \
                    '40259_141942_127969_140066_140593_144250_143059_143491_140351_144608_143923_144484' \
                    '_131423_144278_144880_142205_144900_144003_107315_139910_144106_143477_144966_142426' \
                    '_142912_140311_132921_144238_142112_143861_136752_110085; ' \
                    'BDUSS=5lVnJJOHNxS1NnQnZXa0h4eWRsYmtqamVrMlNEQ0tDcUhDd2xGfmhTYVI4c0ZlRVFBQUFBJCQAAAAA' \
                    'AAAAAAEAAABntKUnvMW-ssmtwdZiYWJ5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
                    'AAAAAAAAAAAAAAAAAJFlml6RZZpeMU; BDUSS_BFESS=5lVnJJOHNxS1NnQnZXa0h4eWRsYmtqamVrMlNEQ0' \
                    'tDcUhDd2xGfmhTYVI4c0ZlRVFBQUFBJCQAAAAAAAAAAAEAAABntKUnvMW-ssmtwdZiYWJ5AAAAAAAAAAAAA' \
                    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJFlml6RZZpeMU; BDORZ=B490B5E' \
                    'BF6F3CD402E515D22BCDA1598; BDRCVFR[PaHiFN6tims]=9xWipS8B-FspA7EnHc1QhPEUf; delPer=0;' \
                    ' BD_CK_SAM=1; PSINO=6; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_PS_PSSID=7540_' \
                    '32606_1465_32572_31660_32046_31709_26350_32583; COOKIE_SESSION=10605_1_7_7_3_7_0_0_7_' \
                    '3_0_2_20636_0_4_0_1599048936_1599028225_1599048932%7C9%2310058_26_1599038282%7C9; H_' \
                    'PS_645EC=6682eK25zVrc6zOj%2FYm%2BgYmFg%2FJKEzduoASRFxruqvY1pXbF1kJ5%2BubfRnA'}
rq = request.Request(url, encode_data, header)
response3 = request.urlopen(rq)
pprint(response3.read().decode('utf8'))


