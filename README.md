# blog_django5
django5+bootstrap5.0
#### 使用的技术

采用Django5+Bootstrap5.0搭建完成；

```
https://highlightjs.org/   实现代码高亮
```

```
https://www.wangeditor.com/ 获取web文本编辑器
```

#### 实现的功能

**登录，注册，发评论，发博客，博客搜索**

#### 本地化需要修改的地方

**1**

主文件“csdn_django”的setting.py中，修改DATABASES:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auth', #修改为自己数据库的名字
        'USER': 'root1', #修改为自己的数据库用户名
        'PASSWORD': 'root123', #修改为自己的数据库密码
        'HOST': 'localhost',
        'PORT': '3306',
    },

}
```

**2**

主文件“csdn_django”的setting.py中，修改EMAIL相关文件:

```
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.qq.com'
EMAIL_PORT=587
EMAIL_HOST_USER='2637431363@qq.com' #修改为你的邮箱
EMAIL_HOST_PASSWORD='kxnvsqxiezzseaej' #修改为你的邮箱授权码
DEFAULT_FROM_EMAIL='2637431363@qq.com' #修改为你的邮箱
```



#### 实现的结果

运行

```
python manage.py runserver
```
