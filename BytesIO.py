#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from io import BytesIO
import click

f = BytesIO()
sO = sys.stdout
sys.stdout.r = f
click.echo('hello world')

content = f.getvalue()
sys.stdout = sO
print(content)