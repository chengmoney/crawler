# requests库的安装方法
- 1 用管理员权限启动cmd
- 2 用pip install requests
    - 如果出现不是外部命令的报错情况,请在系统环境变量-path中添加python安装文件路径及python中scripts文件路径
    - 注意如果还是import引用报错,可能是因为你使用了虚拟环境,需在pycharm中的terminal重新安装
- 3 测试requests
```python
import requests
r = requests.get('http://www.baidu.com')
r.status_code
r.encoding = 'utf-8'

```

# requests 库方法
1. ## requests.get()方法
    - requests.get(url, params=None, **kwargs)
        - url:拟获取页面的url链接
        - params:url中额外参数,字典或字节流格式
        - **kwargs:12个控制访问的参数
        
    - r.status_code http请求的返回状态,200表示连接成功,404表示失败
    - r.text http响应内容字符串形式,url对应的页面内容
    - r.encoding http头中猜测的编码
        - 如果header中不存在charset,则认为编码为iso-8859-1                                                                                                                                                                        
    - r.apparent_encoding 从内容中分析的编码方式
    - r.content 二进制形式

2. ## requests库异常
    | 异常 | 说明 |
    | :---: | :---:|
    | requests.ConnectionError | 网络连接错误异常,如dns查询失败/拒绝连接等 |
    |requests.HTTPError| HTTP错误异常|
    |requests.URLRequired | URL缺失异常 |
    |requests.TooManyRedirects| 超过最大重定向次数,产生重定向异常 |
    | requests.ConnectTimeout | 连接远程服务器超时异常 |
    | requests.Timeout | 请求URL超时,产生超时异常 |
    - r.raise_for_status()  如果不是200,产生异常requests.HTTPError
    - 通用代码框架见 通用代码框架.py
 
    
    

     
  

 

    
    
    