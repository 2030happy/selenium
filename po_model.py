from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
    '''
    基础类，用于页面对象类的继承
    '''

    login_url = 'https://www.epwk.com/login.html'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == self.base_url

    def _open(self):
        self.driver.get(self.base_url)
        assert self.on_page(), 'Did not land on %s' % self.base_url

    def open(self):
        self._open()

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

class LoginPage(Page):
    '''
    epwk登录页面模型
    '''
    # 定位器
    username_loc = (By.ID, "txt_account")
    password_loc = (By.ID, "pwd_password")
    submit_loc = (By.ID, "btn_sub")

    # Action
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

def test_user_login(driver, username, password):
    """
    测试获取的用户名/密码是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()

def main():
    try:
        driver = webdriver.Chrome()
        username = 'username'
        password = 'password'
        test_user_login(driver, username, password)
        sleep(3)
        text = driver.find_element_by_xpath("//span[@class='red']").text
        print(text)
        assert(text == 'you1'), "用户名不匹配，登录失败"
    finally:
        # 关闭浏览器窗口
        driver.close()
if __name__ == '__main__':
    main()
