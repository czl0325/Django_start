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
另外安装mysql，教程：https://www.cnblogs.com/zhangkanghui/p/9613844.html
安装mysql之前windows系统还必须安装visual studio
```

以上步骤都做完后，开始生成迁移文件
python manage.py makemigrations
在生成迁移文件之前你要在数据库中先创建对应的数据库名，这里是CREATE DATABASE book;
生成的迁移文件在booktest/migrations/0001_initial.py中
然后执行迁移
python manage.py migrate
看到一切都OK。可以查看数据库表，发现创建成功。


### 后台管理

#### 1.管理界面本地化
本地化是将显示的语言、时间等使用本地的习惯，这里的本地化就是进行中国化，中国大陆地区使用简体中文，时区使用亚洲/上海时区，注意这里不使用北京时区表示。
打开booktest/settings.py文件，找到语言编码、时区的设置项，将内容改为如下：
```
LANGUAGE_CODE = 'zh-hans' #使用中国语言
TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间
```


#### 2.创建管理员
创建管理员的命令如下，按提示输入用户名、邮箱、密码。
python manage.py createsuperuser
接下来启动服务器。
python manage.py runserver
打开浏览器，在地址栏中输入如下地址后回车。
http://127.0.0.1:8000/admin/
输入用户名密码登录后，可以看到用户和组，但是并没有图书、英雄的管理入口，接下来进行第三步操作



#### 3.注册模型类
登录后台管理后，默认没有我们创建的应用中定义的模型类，需要在自己应用中的admin.py文件中注册，才可以在后台管理中看到，并进行增删改查操作。
打开booktest/admin.py文件，编写如下代码：

```
from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
```

这样就可以进行增删改查了

#### 4.自定义管理页面
在列表页只显示出了BookInfo object，对象的其它属性并没有列出来，查看非常不方便。 Django提供了自定义管理页面的功能，比如列表页要显示哪些值。
打开booktest/admin.py文件，自定义类，继承自admin.ModelAdmin类。
属性list_display表示要显示哪些属性
```
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
```
修改模型类BookInfo的注册代码如下
```
admin.site.register(BookInfo, BookInfoAdmin)
```
刷新BookInfo的列表页，所有属性都显示出来了



### 视图

#### 1.定义视图

视图就是一个Python函数，被定义在views.py中。
视图的必须有一个参数，一般叫request，视图必须返回HttpResponse对象，HttpResponse中的参数内容会显示在浏览器的页面上。
打开booktest/views.py文件，定义视图index如下
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("index")
```


#### 2.配置URLconf

查找视图的过程
请求者在浏览器地址栏中输入url，请求到网站后，获取url信息，然后与编写好的URLconf逐条匹配，如果匹配成功则调用对应的视图函数，如果所有的URLconf都没有匹配成功，则返回404错误。

一条URLconf包括url规则、视图两部分：

url规则使用正则表达式定义。
视图就是在views.py中定义的视图函数。
需要两步完成URLconf配置：

在项目的urls.py文件中定义路径，注意django3.0开始和之前不一样，正则的写法不一样
```
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^index$', views.index),
]
```
如上re_path表示匹配index的路径