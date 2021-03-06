# HELLO RICK

***

### 项目路径GOPATH

* 我的电脑中配置，路径为项目工作目录，goland中配置工作目录，修改后重启终端生效
* 包文件编辑好后，包路径下执行编译和安装，会在src同级目录生成pkg文件

```
1. go build
2. go install（生成pkg）
```

* `go get github.com/manucorporat/try` 也会安装第三包到pkg目录下,如果没有pkg包，会在src下生成
* 执行的文件名为main，到main文件路径进行入口文件编译，然后run





### windows查看进程及杀死进程

* `tasklist | findstr` "进程相关名称"
* `netstat -aon | findstr "5060"` 根据端口查询进程 
* 杀死进程 `taskkill /pid 进程号 /f`

## goland破解

[goland2019.2.3 破解](http://c.biancheng.net/view/6124.html)



## go web

***

* `go fmt github.com/narenaryan/romanserver` (go fmt file_path)
* `go install github.com/narenaryan/romanserver` (go install main_dir)



* supervisord and Gulp
* httprouter
* Gorilla Mux

## windows go web环境搭建

***

* 项目设置到home（自定义的）,home下新建src下，src的上一级为项目根目录home
* src下安置公司项目目录，goland打开到clouddns目录
* clouddns下执行go mod init初始化
* 项目启动运行出现gcc编译错误，下载windows gcc编译软件，添加到环境变量后重启

`# github.com/apache/rocketmq-client-go/core
..\pkg\mod\github.com\apache\rocketmq-client-go@v1.2.4\core\cfuns.go:23:10: fatal error: rocketmq/CMessageExt.h: No such file or directory
   23 | #include <rocketmq/CMessageExt.h>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.`

1. [安装vs2015](https://blog.csdn.net/guxiaonuan/article/details/73775519)
2. `https://github.com/apache/rocketmq-client-cpp/tree/master#build-and-install` 编译安装[rocketmq-client-cpp](https://github.com/apache/rocketmq-client-cpp) 
3. go get github.com/apache/rocketmq-client-go/core



* mysql zip数据库安装

1. [mysql-5.7.21-winx64.zip安装教程](https://blog.csdn.net/we_are_the_world_123/article/details/79230537) 
2. [修改密码](mysql 修改密码报错解决) 
3. [导入数据sql文件](https://blog.csdn.net/davidchengx/article/details/75912013) 



* redis 

1. 下载zip安装包，解压拷贝至c盘，设置环境变量
2. 安装设置windows服务，开机自动自动 `redis-server --service-install redis.windows-service.conf --loglevel verbose` 

## python

* python 指定解释器版本创建虚拟环境 `mkvirtualenv -p c:\\python27\python.exe py27` 
* pip 镜像源配置 `C:\Users\Administrator\AppData\Roaming\pip` 

```
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```



## python pymysql

***

```
import pymysql
import contextlib

# specify db config
host = "127.0.0.1"
port = 3306
db_name = ""
user = ""
passwd = ""


@contextlib.contextmanager
def mysql_connect():
    conn = pymysql.connect(host=host, port=port, user=user, password=passwd, db=db_name, charset='utf8', autocommit=True)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    # for test
    with mysql_connect() as db:
        sql = "select * from gateway"
        db.execute(sql)
        for row in db.fetchall():
            print(row)

```

# how to install Python 3, `pip`, `venv`, `virtualenv`, and `pipenv` on [Red Hat Enterprise Linux](https://developers.redhat.com/products/rhel/overview/) 7   [red hat官方](https://developers.redhat.com/blog/2018/08/13/install-python3-rhel/)

***

```
yum install rh-python36
scl enable
scl enable rh-python36 bash  # 每次进去重新执行
```



## centos 安装python3 编译错误

```
centos6，gcc 4.8.2下出现expecting string instruction after `rep’的错误，解决方法：
```

```
wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O /etc/yum.repos.d/devtools-2.repo

yum install devtoolset-2-gcc devtoolset-2-binutils

yum install devtoolset-2-gcc-gfortran

```

```
安装静态库
# yum install -y openssl-static
安装gcc
# yum install -y gcc wget
# yum groupinstall "Development tools"
# yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

1、通过官网下载Python3安装包
# wget http://python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
2、解压安装包
# tar xf Python-3.6.1.tar.xz
3、编译安装
进入Python-3.6.1文件夹下，进行编辑安装

# ./configure --prefix=/usr/local/python3
# make & make install

添加刚安装的python3版本的文件连接
# ln -s /usr/local/python3/bin/python3(编译安装目录) /usr/bin/python3

添加pip的文件连接
查看pip版本信息

# python3 -m pip -V
pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
注：如果输出提示没有pip，则执行——五、pip的安装
添加pip的文件连接

# ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
查看pip版本信息

# pip3 -V
pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)

```

```
利用python2 安装virtualenvwrapper
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
fi
再次读入.bashrc:

$ source ~/.bashrc
```

## python urllib

* python2

```
import urllib2

values = {"username":"962457839@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
```

* python3

```
from urllib import request
from urllib import parse
from urllib.request import urlopen

values = {'username': '962457839@qq.com', 'password': 'XXXX'}
data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = request.Request(url, data)
response = urlopen(request)
print(response.read().decode())
```

* python2 打印字典

```
import json
a=['阿萨德飞机',123]
print a
print json.dumps(a, ensure_ascii=False, encoding="utf-8")
```

```
json.loads(data, encoding="utf-8")
```

* 命令行入参模板

```
import argparse

#==================================================================
def make_argparse():
  ''' change this function for custom command line parameter.'''

  parser = argparse.ArgumentParser()

  # positional argument : parse by sequance , must be exist, 
  # must in right type , must in right sequance
  parser.add_argument("name", help="--------")          #default type is string
  parser.add_argument("tel",  help="--------",type=int) #custorm int type

  # optional argument : parse by key and value, no care 
  # to sequance , such as "-x=xxxx" or "-x xxxx"
  parser.add_argument("-o", "--output",  help="--------")
  parser.add_argument("-v", "--verbosity", help="--------", action="store_true")
  #This means that, if the option is specified, assign the value True to args.verbosity.
  # Not specifying it implies False.

  args = parser.parse_args()
  return args
#==================================================================

#main code
args = make_argparse(); 
print args.name
print args.tel
if args.verbosity:
  print "verbosity turned on"
if args.output:
  print "output : " + args.output
```



# vim

***

* yy 赋值整行
* p复制到当前下一行，P复制到当前光标上一行
* dd 剪切当前行
* 末行模式输入：set number
* /search_chr，回车后可以使用如下操作, n下一个, N上一个
* 末行模式：`%s/foo/bar/g`会在全局范围(`%`)查找`foo`并替换为`bar`，所有出现都会被替换（`g`）。



# windows cmd

***

* `git log --oneline>>sync.log`
* linux ls > demo.txt

# kafka

***



# mysql user permission

***

* 多对多建表

```
步骤1:创建三张数据表Student ,Course,Stu_Cour

/**学生表*/
CREATE TABLE student (
stu_id INT AUTO_INCREMENT,
NAME VARCHAR(30),
age INT ,
class VARCHAR(50),
address VARCHAR(100),
PRIMARY KEY(stu_id)
)
/*学生课程表*/
CREATE TABLE Course(
cour_id INT AUTO_INCREMENT,
NAME VARCHAR(50),
CODE VARCHAR(30),
PRIMARY KEY(cour_id)
)
/**学生课程关联表*/
CREATE TABLE Stu_Cour(
sc_id INT AUTO_INCREMENT,
stu_id INT ,
cour_id INT,
PRIMARY KEY(sc_id)
)
第二步:为Stu_Cour表添加外键

/*添加外键约束*/
ALTER TABLE Stu_Cour ADD CONSTRAINT stu_FK1 FOREIGN KEY(stu_id) REFERENCES student(stu_id)
ALTER TABLE Stu_Cour ADD CONSTRAINT cour_FK2 FOREIGN KEY(cour_id) REFERENCES Course(cour_id)
```

