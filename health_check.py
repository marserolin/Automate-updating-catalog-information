#!/usr/bin/env python3
import os
import psutil
import shutil
import sys
import socket
import emails

def check_cpu_constrained():
  return psutil.cpu_percent(1) > 80

def check_disk_full():
  du = shutil.disk_usage('/')
  percent_free = 100 * du.free / du.total
  return percent_free < 20

def check_memory():
  mb_available = psutil.virtual_memory().available / (1024 ** 2)
  return mb_available < 500

def check_localhost():
  try:
    socket.gethostbyname('localhost')
    return False
  except:
    return True

def main():
  checks=[
    (check_cpu_constrained, "Error - CPU usage is over 80%"),
    (check_disk_full, "Error - Available disk space is less than 20%"),
    (check_memory, "Error - Available memory is less than 500MB"),
    (check_localhost, "Error - localhost cannot be resolved to 127.0.0.1")
  ]
  everything_ok= True
  for check, msg in checks:
    if check():
      subject = msg
      everything_ok= False

  if not everything_ok:
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ.get('USER'))
    body = 'Please check your system and resolve the issue as soon as possible'
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)
    sys.exit(1)

  print("Everything ok.")
  sys.exit(0)

main()
