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



## go web

***

* `go fmt github.com/narenaryan/romanserver` (go fmt file_path)
* `go install github.com/narenaryan/romanserver` (go install main_dir)



* supervisord and Gulp
* httprouter
* Gorilla Mux
* 