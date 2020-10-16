#!/usr/bin/env python3
import os
import datetime
import reports
import emails

user = os.environ.get('USER')
dir = '/home/{}/supplier-data/descriptions/'.format(user)
paragraph = []
for file in os.listdir(dir):
    with open(dir + file, "r") as text:
        name = text.readline()
        weight = text.readline()
        paragraph.append("name: {}<br/>weight: {}<br/>".format(name, weight))
new_paragraph = '<br/>'.join(paragraph)

today = datetime.date.today()
date_string = today.strftime("%B %d %Y")
title = "Processed Update on {}".format(date_string)
attachment_path = '/tmp/processed.pdf'

if __name__ == "__main__":
    new_paragraph = '<br/>'.join(paragraph)
    reports.generate_report(attachment_path, title, new_paragraph)
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(user)
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)
