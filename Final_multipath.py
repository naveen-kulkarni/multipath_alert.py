#!/usr/bin/python
import re
import os
mpath_ll = os.popen ('multipath -ll')
for mpath_line in mpath_ll:
   mpath_match = re.search("failed|faulty",mpath_line,re.IGNORECASE)
   if mpath_match:
      print "String is ", mpath_line
#else:
 #   print "No match!!"
 mpath_ll.close()

hba_link = os.popen ('adapter_info')
for hba_line in hba_link:
   hba_match = re.search("Bypassed|LinkDown",hba_line,re.IGNORECASE)
   if hba_match:
      print "String is ", hba_line
#else:
 #   print "No match!!"
hba_link.close()

log_msg = open("/var/log/messages", "r+")
for log_line in log_msg:
    log_match = re.search("down|head",log_line,re.IGNORECASE)
    if log_match:
       print " String is ", log_line
log_msg.close()


------
import subprocess
import smtplib
from email.mime.text import MIMEText
threshold = 40
partition = “/”
def report_via_email():
 msg = MIMEText(“Server running out of disk space”)
 msg[“Subject”] = “Low disk space warning”
 msg[“From”] = “admin@example.com”
 msg[“To”] = “test@gmail.com”
 with smtplib.SMTP(“smtp.gmail.com”, 587) as server:
 server.ehlo()
 server.starttls()
 server.login(“gmail_user”,”gmail_password)
 server.sendmail(“admin@example.com”,”test@gmail.com”,msg.as_string())
