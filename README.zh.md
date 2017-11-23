# Starred

[![explain](./minilogo.svg)](https://github.com/chinanf-boy/Source-Explain)

版本

> 1.3.1

[中文版](./README.zh.md)

# 这是一个文件

> starred.py

## 默认的文件头

``` py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys # 输出准备
from io import BytesIO
from collections import OrderedDict # 
import click # 命令行
from github3 import GitHub # with github token use your project  
```
### `bytesio`

> ``BytesIO`` 使用 ``bytes `` 在 ``内存中``，我们创建了一个``bytesio``，然后写一些字节

## ``ordereddict``

使用 有顺序 的 ``dict``

钥匙

```py

## 如果你想留下

键的顺序
```

你可以用`ordereddict`ordereddict例子

``` py
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict的Key是无序的
# d =  {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict的Key是有序的
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

接下来，使用@轻松控制选项

``` py
@click.command() # click init 
@click.option('--username', envvar='USER', help='GitHub username')# github usename ready 
@click.option('--token', envvar='GITHUB_TOKEN', help='GitHub token')# github token ready
@click.option('--sort',  is_flag=True, help='sort by language') # the star project sort
@click.option('--repository', default='', help='repository name') # you ready update project repo name
@click.option('--message', default='update stars', help='commit message') # once time you commit -m "message"
@click.version_option(version='1.3.1', prog_name='starred') # version

```
## 请注意`envvar`

它会得到环境保护`进口操作系统`操作系统。环境得到（'github_token”）。

## 重点来了

``` py
def starred(username, token, sort, repository, message):
# 选项
```

next
``` py
# show the def desc
  """GitHub starred
    creating your own Awesome List used GitHub stars!
    example:
        starred --username maguowei --sort > README.md
"""
```

next
``` py
# 
    if repository:
        if not token:
            click.secho('Error: create repository need set --token', fg='red')
            return
        # get token ready #        *******************              here
        file = BytesIO()
        sys.stdout = file
    else:
    
        file = None
```

next
``` py
gh = GitHub(token=token) # 获得 
stars = gh.starred_by(username) # # 收藏列表
click.echo(desc) # 展示描述
repo_dict = {} # 定义好变量
```

next
``` py
for s in stars:
    language = s.language or 'Others'
    description = html_escape(s.description).replace('\n', '') if s.description else ''
    if language not in repo_dict:
        repo_dict[language] = []
    repo_dict[language].append([s.name, s.html_url, description.strip()])

# 行动是
# repo_dict 拿到了 全部 收藏细节
```

next
``` py
if sort:
    repo_dict = OrderedDict(sorted(repo_dict.items(), key=lambda l: l[0]))

# 变成 有顺序的 ``dict``
```

next
``` py
for language in repo_dict.keys():
    data = u'  - [{}](#{})'.format(language, '-'.join(language.lower().split()))
    click.echo(data)
click.echo('')
# 设置 目录

for language in repo_dict:
    click.echo('## {} \n'.format(language.replace('#', '# #')))
    for repo in repo_dict[language]:
        data = u'- [{}]({}) - {}'.format(*repo)
        click.echo(data)
    click.echo('')

# 语言相关项目

click.echo(license_.format(username=username))

# get License 
```

## why use ``click.echo``

Remember the above ``file`` variable ？

next , show the answer!!;)

``` py
if file:
    rep = gh.repository(username, repository)
    if rep: 
        # 更新
        readme = rep.readme()
        readme.update(message, file.getvalue())
    else:
        # 新建

        # create repo
        rep = gh.create_repository(repository, 'A curated list of my GitHub stars!')
        # create file and 初始化
        rep.create_file('README.md', 'starred initial commit', file.getvalue())
    click.launch(rep.html_url) # 打开浏览器，去 项目网址

```

``` py 
file = BytesIO()
sys.stdout = file

click.echo('something')
# file.getvalue() # something
```

# Or

## Go [Answer!!](./BytesIO.py) and Run , then show ``hello world``

---

完了！！

# MIT
