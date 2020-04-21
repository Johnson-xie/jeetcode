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

