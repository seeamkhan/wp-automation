#!/usr/bin/env python
# coding: utf-8
import Conf_Reader
import os, time, sys
import requests
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders



def email_sender(wp_checker_log):
    print "Sending email, please wait..."
    email_log = ''
    message = []
    email_body = wp_checker_log
    credentials_file = os.path.join(os.path.dirname(__file__), 'login.credentials')
    fromaddr = Conf_Reader.get_value(credentials_file, 'EMAIL_USER')
    email_password = Conf_Reader.get_value(credentials_file, 'EMAIL_PASSWORD')

    # toaddr = ['wpupdate@dev.panth.com', 'seeam@dev.panth.com']
    # toaddr = ['sdteam@dev.panth.com']
    toaddr = ['panth.me@gmail.com']
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    # msg['To'] = toaddr
    ", ".join(toaddr)
    msg['Subject'] = "RTH Toolkit WordPress WordPress Update Notification Email"

    msg.attach(MIMEText(email_body, 'plain'))

    # FOR ATTCAHMENTS
    filename = "test.jpg"
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.jpg')
    attachment = open(file_path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)
    # END OF Attachments change

    server = smtplib.SMTP('dev.panth.com', 25) # 587 was 25 previously
    server.starttls()
    server.login(fromaddr, email_password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print 'Email Sent.'

message = "Test email content"
email_sender(message)