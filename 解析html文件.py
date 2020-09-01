from bs4 import BeautifulSoup
import requests
url = 'http://python123.io/ws/demo.html'
kv = {'user-agent': 'mozilla/5.0'}
try:
    r = requests.get(url, headers=kv)
    # r = requests.get(url)
    r.raise_for_status()
    demo = r.text
except:
    print('爬取失败')

# 创建BeautifulSoup对象
soup = BeautifulSoup(demo, 'html.parser')
# 用HTML格式打印出来
print(soup.prettify())
# 查看p标签的属性,返回字典类型
print('\np标签的属性:%s' % soup.p.attrs)
print(soup.p.attrs['class'])
# 查看p标签
print(soup.p)
# 查看p标签的内容
print('\n' + soup.p.string)

# 遍历子节点 -contents/children/descendants
# --------contents用 列表 列出所有的子节点
print(soup.html.contents)
# --------children 列出所有子节点的迭代形式
print(soup.html.children)  # list_iterator
for child in soup.html.children:
    print(child)
print('-----------------------------------------------------------')
# --------descendants 子孙节点都显示，迭代形式
ls = []
for child1 in soup.html.descendants:
    ls.append(child1)
print(ls)
print('-----------------------------------------------------------')

# 遍历父节点 -parent/parents
# --------parent 节点的父节点 --包含自己
print(soup.html.parent)
print('-----------------------------------------------------------')
print(soup.title.parent)
# --------parents 节点的先辈标签
print('---------------------parents 节点的先辈标签---------------------------')
for pr in soup.title.parents:
    print(pr.name, end='------\n')

# 遍历平行节点
# ----next_sibling 下一个平行节点/next_siblings 后续的所有平行节点  previous_sibling 上一个平行节点 previous_siblings 前续所有的平行节点
print('--------------------下一个平行节点/next_sibling----------------------')
print(soup.p.next_sibling)
print('--------------------后续所有平行节点/next_siblings----------------------')
ls = []
for pr in soup.p.next_siblings:
    ls.append(pr)
print(ls)
print('--------------------上一个平行节点/previous_sibling----------------------')
print(soup.a.previous_sibling)
print('--------------------前续所有平行节点/previous_siblings----------------------')
ls = []
for pr in soup.a.previous_siblings:
    ls.append(pr)
print(ls)

