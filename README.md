# AOE

## 项目简介
* 使用airtest和poco为框架进行搭建，采用po模型，数据驱动和关键字驱动进行封装，结果采用allure报告，支持jenkins调用
* 示例代码使用百度地图为例，使用airtest-selenium测试百度地图web端，poco测试百度地图app端和微信小程序，request测试百度地图api
## 功能特性
* 可以用它测试web，app，h5，api
## 环境依赖
* 需要python3.7
* 测试微信小程序，还需要下载tbs内核，打开微信中任意一个聊天框，输入 debugtbs.qq.com，点击进入TBS调试页面，再点击页面内的“安装线上内核”，然后重启微信，之后poco即可抓取小程序界面的元素
## 部署步骤
* 使用docker+jeknins部署至服务器
* docker pull jenkins/jenkins
* mkdir -p /home/ubuntu/jenkins_mount
* chmod 777 /home/ubuntu/jenkins_mount
* docker run -d -p 7080:8080 -p 7081:50000 -v /home/ubuntu/jenkins_mount:/var/jenkins_home -v /etc/localtime:/etc/localtime --name myjenkins jenkins/jenkins
* cd /home/ubuntu/jenkins_mount/
* vim  hudson.model.UpdateCenter.xml
* https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
* 启动jenkins后构建job，新建cases参数
* 执行内容写入：python runner/case_runner.py --cases=${cases}
* 运行时只需传入case参数
## 目录结构描述
* case 用例集合，包含web,app,applet,api所有用例
* common 公用类，包含各项目的po基类base_page，和各项目的测试基类test_base_case，
* data yaml数据，包含数据驱动所有需要的yaml文件和持久化配置文件shelve数据
* log 日志文件，所有log打印
* page po模型，所有项目的page页面
* report 报告，用例结束后的allure报告
* runner 运行入口，运行用例的启动入口，支持传参case，一般用于jenkins调用
* utils 基础方法，与page和case无关的基础方法，可被所有模块调用
## 版本内容更新
## 声明
## 协议
