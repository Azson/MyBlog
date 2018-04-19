import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#发送邮件需要保证内容有意义，否则，腾讯的邮箱服务器会拒绝接受
class EmailClass:

    def sendEmail(text, user_client):
        user_send_account = "18390208501@163.com"
        user_send_code = "jay240326315"
        try:
            msg = MIMEText(str(text), 'plain', 'utf-8')
            msg['From'] = formataddr(["AzsonWeb", user_send_account])
            # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["AzsonHost", "240326315@qq.com"])
            # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "你好！"
            # 邮件的主题，也可以说是标题
            #if (dataInfo['my_sender'].split('@')[1] == "qq.com"):
            #    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            #elif (dataInfo['my_sender'].split('@')[1] == "163.com"):
            server = smtplib.SMTP_SSL("smtp.163.com", 465)

            # 发件人邮箱中的SMTP服务器，端口是25
            #print("user: {0}\ncode:{1}\nto:{2}".format(dataInfo['my_sender'], dataInfo['my_pass'], dataInfo['my_user']))

            server.login(user_send_account, user_send_code)
            print(msg.as_string())
            # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(user_send_account, ["240326315@qq.com", ], msg.as_string())
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()
            print("发送成功！")
        except Exception as e:
            print(e)
            print("发送失败！")
            return False
        return True