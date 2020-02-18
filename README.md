# Django_start
第一个django起步小项目，新建django项目，配置mysql，sql语句操作，MVT基本操作。


### 1.起步

```
pip3  --default-timeout=1000000 install django
```

cd  到项目目录，创建项目
```
django-admin startproject 项目名称
```
如果找不到django路径，尝试
```
python3 /Users/zhaoliangchen/Library/Python/3.7/lib/python/site-packages/django/bin/django-admin.py startproject book_project
```
在book_project中，包含文件
manage.py是项目管理文件，通过它管理项目。
_init_.py是一个空文件，作用是这个目录book_project可以被当作包使用。
settings.py是项目的整体配置文件。
urls.py是项目的URL配置文件。
wsgi.py是项目与WSGI兼容的Web服务器入口

cd book_project
创建一个app： 
```
python3 manage.py startapp booktest
```

booktest内包含
_init.py    _是一个空文件，表示当前目录booktest可以当作一个python包使用。
tests.py    用于开发测试用例，在实际开发中会有专门的测试人员，这个事情不需要我们来做。
models.py   文件跟数据库操作相关。
views.py    文件跟接收浏览器请求，进行处理，返回页面相关。
admin.py    文件跟网站的后台管理相关。
migrations  生成ORM迁移文件


#### 安装应用

应用创建成功后，需要安装才可以使用，也就是建立应用和项目之间的关联，在book_project/settings.py中INSTALLED_APPS下添加应用的名称就可以完成安装

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest',
]
```

#### 运行服务器

python manage.py runserver 
运行成功后可以在http://127.0.0.1:8000 查看，默认是8000端口，可以自行设置端口，如
python manage.py runserver 127.0.0.1:8001


### 2.把数据库切换成mysql

django自带的数据库是sqlite，我们要切换成mysql

首先安装pymysql
pip3 install pymysql


在项目booktest的setting.py文件中设置mysql，把之前sqlite的代码注释掉，如下：
```
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'book',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```

在__init__.py中加入如下代码：
```
import pymysql
pymysql.install_as_MySQLdb()
```


```
出现错误：mysqlclient 1.3.13 or newer is required; you have 0.9.3.
参考解决方法：https://blog.csdn.net/lijing742180/article/details/91966031
```


