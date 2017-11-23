# starred

[![explain](./minilogo.svg)](https://github.com/chinanf-boy/Source-Explain)

版本
> 1.3.1

[中文版](./README.zh.md)

# this is one file

> starred.py

## file head default

``` py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys # get the config file
from io import BytesIO
from collections import OrderedDict # 
import click # cmd options good project
from github3 import GitHub # with github token use your project  
```

### ``BytesIO``

> ``BytesIO`` read and write ``bytes ``in`` memory``, we create a BytesIO, and then write some bytes

### ``OrderedDict``

> ``Key`` is unordered when using ``dict``. When iterating on ``dict``, we can not determine the order of the ``keys``.

> If you want to keep ``the order of Key``, you can use ``OrderedDict``

OrderedDict example

``` py
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict的Key是无序的
# d =  {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict的Key是有序的
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

## next , use the @click easy control options

``` py
@click.command() # click init 
@click.option('--username', envvar='USER', help='GitHub username')# github usename ready 
@click.option('--token', envvar='GITHUB_TOKEN', help='GitHub token')# github token ready
@click.option('--sort',  is_flag=True, help='sort by language') # the star project sort
@click.option('--repository', default='', help='repository name') # you ready update project repo name
@click.option('--message', default='update stars', help='commit message') # once time you commit -m "message"
@click.version_option(version='1.3.1', prog_name='starred') # version

```

Please note ``envvar`` , it will get env
``` py
import os
os.environ.get('GITHUB_TOKEN')
```

## main def

``` py
def starred(username, token, sort, repository, message):
# the options is above @click.option s
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
gh = GitHub(token=token) # get github 
stars = gh.starred_by(username) # # get username stars list
click.echo(desc) # show the desc
repo_dict = {} # ready the define
```

next
``` py
for s in stars:
    language = s.language or 'Others'
    description = html_escape(s.description).replace('\n', '') if s.description else ''
    if language not in repo_dict:
        repo_dict[language] = []
    repo_dict[language].append([s.name, s.html_url, description.strip()])

# in the for action
# repo_dict is get all stars message from username
```

next
``` py
if sort:
    repo_dict = OrderedDict(sorted(repo_dict.items(), key=lambda l: l[0]))

# become order dict, we tolk
```

next
``` py
for language in repo_dict.keys():
    data = u'  - [{}](#{})'.format(language, '-'.join(language.lower().split()))
    click.echo(data)
click.echo('')
# set repo - menu 

for language in repo_dict:
    click.echo('## {} \n'.format(language.replace('#', '# #')))
    for repo in repo_dict[language]:
        data = u'- [{}]({}) - {}'.format(*repo)
        click.echo(data)
    click.echo('')

# set single language with Detail

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
        # down here was update Star list
        readme = rep.readme()
        readme.update(message, file.getvalue())
    else:
        # down here was the first create repository

        # create repo
        rep = gh.create_repository(repository, 'A curated list of my GitHub stars!')
        # create file and git init commit message
        rep.create_file('README.md', 'starred initial commit', file.getvalue())
    click.launch(rep.html_url) # open browser to url

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

Done!

# MIT
