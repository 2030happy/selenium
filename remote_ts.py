from selenium.webdriver import Remote

"""
要想在其他主机上启动node，则必须满足以下要求：
本地hub主机与远程node主机之间可以用ping命令连通；
远程主机必须安装用例执行的浏览器及驱动，并且驱动要放在环境变量path的目录下；
远程主机必须安装Java环境，因为需要运行Selenium Server。

执行程序前先启动hub和远程node
1.启动本地hub主机（本地主机IP为：172.16.10.66）
java -jar selenium-server-standalone-3.11.0.jar -role hub
2.启动远程node主机（IP地址：172.16.10.34）
java -jar selenium-server-standalone-3.11.0.jar -role node -port 5555 -hub http://172.16.10.66:4444/grid/register

"""

# 定义主机与浏览器
lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
         'http://127.0.0.1:5555/wd/hub': 'internet explorer',
         'http://127.16.10.34:5555/wd/hub': 'firefox'
         }

# 通过不同的浏览器执行脚本
for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser,
                                          'version': '',
                                          'javascriptEnabled': True
                                          }
                    )
    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys("remote")
    driver.find_element_by_id("su").click()

    driver.close()