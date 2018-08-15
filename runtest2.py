from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib, unittest, time, os

# ===============定义发送邮件==================
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("username@qq.com", "SMTP授权码")
    smtp.sendmail("username@qq.com", "receiver@163.com", msg.as_string())
    smtp.quit()
    print('email has send out !')

# =========查找测试报告目录，找到最新生成的测试报告文件===========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    test_dir = 'E:\\python_workspace\\selenium\\test_project\\test_case'
    test_report = 'E:\\python_workspace\\selenium\\test_project\\report'

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)  #发送测试报告
