
# 一 环境搭建
> 1. [安装Jdk8](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html) 并添加全局环境变量  
> 注：javac验证是编译器， java是解释器
> 2. [安装Tomcat(应用服务器)](https://tomcat.apache.org/download-80.cgi) 下载8 Core中的版本即可  
> 注：将压缩包解压放在文件夹下即可，然后点击bin/startup.bat(windows下)即可。若报错，解决办法如下：
>   1. cmd下cd xx/bin/下 -> service.bat install
>   2. service remove tomcat8
>   3. 在次点击startup.bat (https://blog.csdn.net/wxb141001yxx/article/details/96976380)
>   4. 浏览器输入localhost:8080即可验证tomcat启动是否成功
>   5. 修改startup.bat & shutdown.bat 在开头添加环境变量  
>       JAVA_HOME = C:\Program Files\Java\jdk1.8.0_271  
>       TOMCAT_HOME = C:\Program Files\apache-tomcat-8.5.60
> 3. [安装数据库mysql](https://dev.mysql.com/downloads/windows/installer/5.7.html)  
>    注：[安装链接](https://www.jianshu.com/p/c402c563d81e)
>        MySQL服务名称：MySQL57, 密码123456
> 4. [安装JPress](http://www.jpress.io/download)  
>   注： 下载JPress的war包，只需要一个war包即可。将war包解压放到xx/tomcat/webapps/目录下，最好修改名称为jpress,
>       否则在浏览器中输入名称的时候，将要输入完整的路径名称(localhost:8080/jpress)
> 5. 至此环境搭建已完成，创建数据库(create database se_test)
> 6. 进行jpress的网站初始化

# 二 安装python模块
> `pip install unittest`  
> `pip install selenium`  
`pip install pytesseract` # 将简单图片中内容转化为字符串  
`pip install pil` # python2, 图片截取
`pip install pillow`  # python3安装  
`pip install PyAutoGUI`   # 通过坐标控制鼠标和键盘进行点击操作  
>`pip install requests`
>`pip install pytest`
>`pip install allure-pytest` 
> [allur下载](https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/)
> pytest --alluredir reports testcase/pytest/test6.py
> allure serve reports  # 命令执行生成测试报告进行展示
> `pip install pytest-dependency`
> `pip install mysqlclient`
> `pip install xcode`


# 三 解析验证码
> 1. [登录ShowApi](https://www.showapi.com/apiGateway/view/184/4)
> 2. 下载SDK, 导入py库文件, 然后进行测试



POM：Page Object Module 页面对象模型
DDT: Data Driver Tests 数据驱动