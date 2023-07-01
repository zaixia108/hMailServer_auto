import sys
from clr import AddReference

AddReference(r'E:\hMail\hMailDLL.dll')
from hMailDLL import *

obj = Email()
import pythonnet

from imbox import Imbox


def add_account(address, password):
    obj.addUser(address, password)

# 邮件信息
def send_mail(address, password, content, target_mail):
    """
    发送邮件
    :param address: 你的邮件地址，例：test@auto108.info
    :param password: 你的密码，例：test123
    :param mailinfo: 你的邮件内容，例：i am body
    :param target_mail: 谁要接受邮件
    :return: None
    """
    mailinfo = obj.MailInfo()
    mailinfo.From = address  # 发件人
    mailinfo.to = target_mail  # 收件人
    mailinfo.subject = "nothing"  # 邮件主题
    mailinfo.body = content  # 邮件内容

    print(obj.sendmail(address, password, mailinfo))


def get_mail(f2a=False):
    with Imbox('154.9.227.66', username='test@auto108.info', password='test123', ssl=False, ssl_context=None,
               starttls=False) as i:
        all_mails = i.messages()
        # for uid, messages in all_mails:
        #     print(messages.subject)
        #     # 输出邮件主题
        #     print(messages.body)
        #     # 输出邮件内容以文本格式
        #     print(uid)
        new_mails = all_mails[1][1]
        # print(new_mails)
        if f2a:
            content = new_mails.body['html']
            content = str(content)
            import re
            content = re.findall(r"\d+\.?\d*", content)
            # 取出第一个数字
            result = []
            for i in content:
                if len(i) == 6:
                    result.append(i)
            print(result)
        else:
            content = new_mails.body['plain']
            content = str(content)
            # 取出content中的链接
            import re
            content = re.findall(r"https://.*?\"", content)
            result = []
            link = []
            for i in content:
                result.append(i[:-1])
            for i in result:
                if "verifymail" in i:
                    link.append(i)
            print(link[0])


# get_mail()
# send_mail('test@auto108.info', 'test123', 'test', '1029310297@qq.com')
