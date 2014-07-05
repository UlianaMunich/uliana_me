from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6', 'south', 'psycopg2', 'pygments', 'pagedown', 'django-pagedown', 'markdown']

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='Uliana.me',
      version='2.0',
      description='My Personal Site',
      author='Uliana',
      author_email='',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

